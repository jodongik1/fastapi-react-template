# 한국투자증권 (KIS) Open API 연동 가이드 (docs/profiles/kis-broker.md)

> ℹ️ **안내**: 본 문서는 **한국투자증권(KIS) Open API를 연동하여 국내/해외 주식 시세, 캔들 데이터, 잔고 및 주문 기능을 구축할 때 준수해야 하는 공식 개발 가이드**입니다.

---

## 1. 공식 참조 링크 및 명세
- **공식 API 개발자 포털**: [KIS Developers Portal](https://apiportal.koreainvestment.com/apiservice-apiservice)
- **공식 GitHub 샘플 코드**: [koreainvestment/open-trading-api](https://github.com/koreainvestment/open-trading-api)

---

## 2. 서버 환경 및 엔드포인트 도메인 규격

KIS API는 실전투자(Production)와 모의투자(Virtual/Paper)의 도메인과 포트가 분리되어 있습니다:

| 구분 | REST API 도메인 | 웹소켓(WebSocket) 도메인 |
| :--- | :--- | :--- |
| **실전투자 (`prod`)** | `https://openapi.koreainvestment.com:9443` | `ws://ops.koreainvestment.com:21000` |
| **모의투자 (`vps`)** | `https://openapivts.koreainvestment.com:29443` | `ws://ops.koreainvestment.com:31000` |

---

## 3. 인증 및 OAuth 접근 토큰(Access Token) 발급 규칙

### 1) 토큰 발급 API 규격 (`POST /oauth2/tokenP`)
- **요청 Body**:
  ```json
  {
    "grant_type": "client_credentials",
    "appkey": "YOUR_APP_KEY",
    "appsecret": "YOUR_APP_SECRET"
  }
  ```
- **응답 규격**:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1Ni...",
    "token_type": "Bearer",
    "expires_in": 86400
  }
  ```

### 2) 🚨 핵심 운영 규칙 (Rate Limit 방어)
- **접근 토큰 유효기간**: **24시간 (86,400초)**
- **매 API 호출마다 토큰을 발급받으면 절대 안 됩니다!** (초당 토큰 발급 제한으로 즉시 계정 차단됨)
- 발급받은 토큰은 반드시 **인메모리 또는 Redis에 캐싱**하고, **만료 1시간 전(23시간 경과 시)에만 백그라운드 갱신**합니다.

---

## 4. 필수 공통 HTTP 요청 헤더 (Headers)

모든 KIS REST API 호출 시 아래 헤더가 정확히 포함되어야 합니다:

```http
Content-Type: application/json; charset=utf-8
authorization: Bearer {access_token}
appkey: {KIS_APP_KEY}
appsecret: {KIS_APP_SECRET}
tr_id: {거래ID}
custtype: P
```

> **거래ID (`tr_id`) 주의사항**:
> KIS API는 모의투자와 실전투자의 `tr_id` 코드가 다릅니다.  
> 예: 국내주식 주문 시 실전은 `TTTC0802U`, 모의투자는 `VTTC0802U`

---

## 5. 주요 거래별 `tr_id` 및 API 엔드포인트 매핑

### 1) 주식 현재가 시세 조회 (`FHKST01010100`)
- **엔드포인트**: `GET /uapi/domestic-stock/v1/quotations/inquire-price`
- **파라미터**:
  - `FID_COND_MRKT_DIV_CODE`: `J` (주식/ETF/ETN)
  - `FID_INPUT_ISCD`: `005930` (삼성전자 6자리 종목코드)
- **주요 응답 필드**:
  - `stck_prpr`: 현재가
  - `prdy_vrss`: 전일 대비 등락금액
  - `prdy_ctrt`: 전일 대비 등락률
  - `acml_vol`: 누적 거래량
  - `acml_tr_pbmn`: 누적 거래대금

### 2) 주식 캔들스틱 차트 조회 (일/주/월/년봉) (`FHKST01010400`)
- **엔드포인트**: `GET /uapi/domestic-stock/v1/quotations/inquire-daily-price`
- **파라미터**:
  - `FID_COND_MRKT_DIV_CODE`: `J`
  - `FID_INPUT_ISCD`: 종목코드
  - `FID_PERIOD_DIV_CODE`: `D`(일봉), `W`(주봉), `M`(월봉)
  - `FID_ORG_ADJ_PRC`: `0`(수정주가 반영)
- **응답 데이터 (`output`)**:
  - `stck_bsop_date`: 영업일자 (`YYYYMMDD`)
  - `stck_oprc`: 시가 (Open)
  - `stck_hgpr`: 고가 (High)
  - `stck_lwpr`: 저가 (Low)
  - `stck_clpr`: 종가 (Close)
  - `acml_vol`: 거래량 (Volume)
  - ⚠️ `lightweight-charts` 형식(`{ time: 'YYYY-MM-DD', open, high, low, close }`)으로 파싱하여 프론트엔드로 반환.

### 3) 국내주식 현금 주문 (매수/매도)
- **실전투자 `tr_id`**: 매수(`TTTC0802U`), 매도(`TTTC0801U`)
- **모의투자 `tr_id`**: 매수(`VTTC0802U`), 매도(`VTTC0801U`)
- **엔드포인트**: `POST /uapi/domestic-stock/v1/trading/order-cash`
- **Body**:
  ```json
  {
    "CANO": "43525227",           // 계좌번호 앞 8자리
    "ACNT_PRDT_CD": "01",        // 계좌상품코드 2자리 (종합계좌: 01)
    "PDNO": "005930",            // 종목코드
    "ORD_DVSN": "00",            // 주문구분 (00: 지정가, 01: 시장가)
    "ORD_QTY": "10",             // 주문 수량
    "ORD_UNPR": "70000"          // 주문 단가 (시장가일 경우 "0")
  }
  ```

### 4) 계좌 잔고 및 예수금 조회
- **실전투자 `tr_id`**: `TTTC8434R`
- **모의투자 `tr_id`**: `VTTC8434R`
- **엔드포인트**: `GET /uapi/domestic-stock/v1/trading/inquire-balance`

---

## 6. 전체 API 인벤토리 및 카탈로그 링크

공식 샘플 코드 저장소(`koreainvestment/open-trading-api`)를 전수 분석하여 정제한 **전체 333개 API 인벤토리(REST 273개, WebSocket 60개)**의 상세 목록(함수명, 한글 기능명, 엔드포인트, 실시간 TR ID 매핑)은 [docs/profiles/kis-api-catalog.md](kis-api-catalog.md)에 상세히 정리되어 있습니다.

### 카테고리별 제공 현황 요약
| 카테고리 | REST API | WebSocket | 합계 | 주요 지원 기능 |
| :--- | :---: | :---: | :---: | :--- |
| **인증 (`auth`)** | 2 | 0 | 2 | OAuth 접근토큰 발급(`tokenP`), 웹소켓 접속키 발급(`Approval`) |
| **국내주식 (`domestic_stock`)** | 130 | 25 | 155 | 현재가/호가/체결, 일/주/월/분봉 캔들, 현금/신용 주문, 정정/취소, 잔고/예수금, 조건검색, 순위분석, 프로그램매매, 공매도/대차 |
| **해외주식 (`overseas_stock`)** | 46 | 4 | 50 | 미국/아시아 현재가, 일/주/월/분봉 차트, 해외주식 주문/정정/취소, 체결내역, 외화 잔고 |
| **국내선물옵션 (`domestic_futureoption`)** | 23 | 20 | 43 | 지수선물/옵션 시세, 야간선물, 주문/정정/취소, 미결제약정, 증거금 상세 |
| **해외선물옵션 (`overseas_futureoption`)** | 31 | 4 | 35 | CME 등 해외선물 시세, 일/주/월 차트, 주문, 미결제/예탁금 잔고 |
| **국내채권 (`domestic_bond`)** | 15 | 3 | 18 | 장내 일반채권 시세/호가, 단가조회, 채권 매수/매도 주문 |
| **ETF / ETN (`etfetn`)** | 5 | 1 | 6 | NAV 괴리율 추이, 구성종목 시세, ETF 실시간 체결 |
| **ELW (`elw`)** | 21 | 3 | 24 | 지표/민감도(델타, 감마 등), 변동성 추이, 순위분석, ELW 호가/주문 |
| **합계** | **273** | **60** | **333** | **전 상품군 지원** |

> 📌 **전체 333개 API의 상세 엔드포인트 및 TR ID 매핑표**: [docs/profiles/kis-api-catalog.md](kis-api-catalog.md) 참조

---

## 7. 백엔드 구현 아키텍처 (`backend/app/services/brokers/kis/`)

FastAPI 백엔드에서 KIS API 연동 시 아래 레이어 패턴을 준수합니다:

```text
backend/app/services/brokers/kis/
├── client.py        # httpx 기반 비동기 KIS HTTP 통신 클라이언트 (토큰 캐싱, 공통 헤더 주입)
├── auth.py          # OAuth 접근 토큰 발급 및 수명주기 관리
├── quote.py         # 현재가, 호가, 캔들 데이터 조회 및 도메인 모델 변환
└── order.py         # 매수/매도 주문 실행, 취소, 잔고 조회
```

### 비동기 통신 및 예외 처리 원칙
1. **비동기 클라이언트**: 모든 통신은 `httpx.AsyncClient`를 사용하여 FastAPI의 비동기 이벤트 루프를 블로킹하지 않습니다.
2. **Rate Limit 방어**: KIS는 초당 요청 제한(초당 약 5회~10회)이 있으므로, 비동기 `asyncio.Semaphore(5)` 또는 0.2초 딜레이를 적용하여 과도한 동시 요청을 방어합니다.
3. **타임아웃 설정**: 주식 장 시작/마감 시간대 KIS 서버 지연을 고려하여 `timeout=10.0`초를 기본으로 설정합니다.
