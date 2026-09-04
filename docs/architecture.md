# 전체 시스템 아키텍처 및 디렉토리 구조 명세 (docs/architecture.md)

본 문서는 **React SPA + FastAPI + PostgreSQL** 스타터 템플릿의 디렉토리 구조, 계층별 책임, API 규격 및 오류 응답 표준을 정의합니다.

---

## 1. 프로젝트 디렉토리 구조 및 책임

```text
.
├── AGENTS.md                  # AI 에이전트 작업 헌법 및 검증 명령
├── CLAUDE.md -> AGENTS.md     # Claude Code 연동 심볼릭 링크
├── .cursorrules -> AGENTS.md  # Cursor IDE 연동 심볼릭 링크
├── docker-compose.yml         # 로컬 개발용 컨테이너 오케스트레이션
├── .env.example               # 환경변수 계약서
├── .node-version              # Node.js 런타임 버전 고정
├── .python-version            # Python 런타임 버전 고정
│
├── docs/                      # 상세 설계 및 도메인 프로필 문서
│   ├── architecture.md        # [본 문서] 디렉토리 구조 및 API 표준
│   ├── security.md            # 인증, 암호화, 세션 보안
│   └── profiles/              # 도메인 확장 모듈 (선택 적용)
│       ├── financial-ledger.md# 금융 정밀도, 원장 보존, 감사 로그
│       └── kis-broker.md      # 한국투자증권(KIS) Open API 연동 및 tr_id 규격
│
├── scripts/
│   └── verify.sh              # 에이전트 단일 검증 진입점 스크립트
│
├── frontend/                  # React + Vite + Tailwind (TypeScript)
│   ├── src/
│   │   ├── components/        # 전역 재사용 UI 컴포넌트 (Button, Modal, Input)
│   │   ├── layouts/           # 화면 공통 레이아웃 (DashboardLayout: Sidebar + Header)
│   │   ├── pages/             # 메뉴/라우트별 화면 컴포넌트 (DashboardPage, SettingsPage 등)
│   │   ├── routes/            # React Router 중첩 라우팅 정의 (AppRoutes.tsx)
│   │   ├── features/          # 도메인/기능별 비즈니스 모듈
│   │   ├── services/          # Axios 인스턴스 및 공통 API 클라이언트
│   │   └── types/             # TypeScript 인터페이스
│   ├── Dockerfile             # 프론트엔드 컨테이너 빌드 파일
│   └── package.json           # 의존성 정의
│
└── backend/                   # Python FastAPI
    ├── app/
    │   ├── api/v1/            # HTTP 요청 라우터 (Controller)
    │   ├── core/              # 전역 설정(config.py), 보안 유틸
    │   ├── models/            # SQLAlchemy 2.0 DB 엔티티
    │   ├── schemas/           # Pydantic v2 요청/응답 검증 스키마
    │   ├── services/          # 순수 비즈니스 로직 계층
    │   ├── repositories/      # DB 쿼리(CRUD) 계층
    │   └── db/                # 세션 관리 (session.py)
    ├── alembic/               # DB 마이그레이션 스크립트
    ├── Dockerfile             # 백엔드 컨테이너 빌드 파일
    └── pyproject.toml         # Python 의존성 및 툴 설정 (uv)
```

---

## 2. API 표준 계약 (API Standards)

### 1) URL 및 버전 관리
- 모든 API는 `/api/v1/` 프리픽스를 사용합니다.
- 복수형 명사를 기본으로 사용합니다 (예: `/api/v1/users`, `/api/v1/items`).

### 2) 표준 에러 응답 형식 (RFC 7807 호환)
모든 API 에러는 일관된 JSON 구조로 반환합니다:
```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "요청 데이터가 올바르지 않습니다.",
    "details": [
      {
        "field": "email",
        "reason": "올바른 이메일 형식이 아닙니다."
      }
    ],
    "timestamp": "2026-09-04T14:00:00Z"
  }
}
```

### 3) 날짜 및 시간 표준
- 데이터베이스 및 API 입출력의 모든 날짜/시간은 **UTC(ISO-8601)** 표준(`YYYY-MM-DDTHH:mm:ssZ`)을 사용합니다.
