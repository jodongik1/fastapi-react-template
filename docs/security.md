# 보안, 자격증명 암호화 및 인증 아키텍처 (docs/security.md)

본 문서는 프로젝트의 민감 정보 암호화, 비밀번호 및 PIN 해싱, JWT 세션 보안, 멱등성(중복 방지) 및 감사 로그 표준을 정의합니다.

---

## 1. 자격증명 암호화 vs 해싱 표준

시스템에서는 **복호화가 필요한 정보**와 **절대 복호화되어서는 안 되는 정보**를 철저히 분리하여 다른 알고리즘을 적용합니다.

### 1) 비밀번호 및 거래/간편 PIN — 단방향 해싱 (Bcrypt)
- **절대 복호화 가능한 대칭키로 암호화하지 않습니다.**
- **저장 표준**: `passlib[bcrypt]` (Bcrypt 솔트 해싱, Cost Factor 12)
- **보안 제약**:
  - 5회 연속 PIN/비밀번호 불일치 시 계정/기능 잠금 처리 (`is_locked = True`)
  - 로그인이나 민감 작업 성공 시 단기 유효 토큰 발급

### 2) 외부 API Key & Secret — 양방향 암호화 (AES-256-GCM)
- 외부 서드파티 서비스(결제사, 증권사, 외부 API 등) 통신을 위해 원문 복호화가 불가피한 자격증명에 적용합니다.
- **암호화 표준**: **AES-256-GCM** (인증 태그 포함, 위변조 방지)
  - 암호문 포맷: `v1:{nonce_base64}:{ciphertext_base64}:{tag_base64}`
  - **Nonce 재사용 절대 금지**: 매 암호화 시마다 12바이트 암호학적 난수(`os.urandom(12)`) 생성.
- **키 관리 (Key Management)**:
  - **로컬 개발**: `.env`의 `MASTER_ENCRYPTION_KEY` (32바이트 Base64 문자열) 허용.
  - **운영(Production)**: AWS KMS 또는 HashiCorp Vault와 같은 Secret Manager 환경 활용 권장.

---

## 2. 인증/인가 및 네트워크 안전 수칙 (Auth & Network)

### 1) 401 Silent Refresh 시 중복 요청 방지 원칙
프론트엔드 Axios 인터셉터는 401 Unauthorized 발생 시 토큰을 재발급받은 뒤 원래 실패했던 요청을 자동 재전송할 수 있습니다.  
**하지만 결제나 변경(CUD) 요청에 이를 무분별하게 적용하면 이중 처리 사고가 발생합니다.**

- **Axios 요청 메타데이터 규격**:
```typescript
interface CustomAxiosRequestConfig extends AxiosRequestConfig {
  retryAfterRefresh?: boolean; // 기본값: GET 요청은 true, POST/PUT/DELETE는 false 권장
}
```
- **판별 규칙**:
  - `retryAfterRefresh === false`인 중요한 요청은 401 발생 시 토큰을 갱신하더라도 **절대 자동으로 재전송하지 않습니다.**
  - 클라이언트는 사용자에게 "인증 세션이 갱신되었습니다. 내용을 확인하고 다시 시도해주세요." 안내를 제공합니다.

### 2) Refresh Token Rotation (RTR) 및 탈취 탐지
- Refresh Token은 1회용으로 관리하며, 갱신 요청 시마다 새로운 Refresh Token으로 교체(Rotate)합니다.
- 이미 사용된 옛날 Refresh Token이 다시 제출되면 **"토큰 탈취 사고"**로 간주하고 해당 유저의 모든 활성 세션을 즉시 강제 로그아웃 처리합니다.
- 쿠키 속성: `HttpOnly; Secure; SameSite=Lax; Path=/api/v1/auth`

### 3) 소셜 로그인 OAuth 2.0 PKCE & CSRF 방어
- 소셜 로그인 플로우 진행 시 `state` 파라미터(CSRF 방지)와 PKCE(`code_challenge`, `code_verifier`)를 적용하여 인가 코드 가로채기를 원천 방어합니다.
- 백엔드에 등록된 Redirect URI Allowlist 외의 경로로는 코드를 교환하지 않습니다.

---

## 3. 요청 멱등성 보장 (Idempotency)

네트워크 지연, 사용자 더블 클릭, 재전송 공격으로 인한 중복 트랜잭션을 원천 차단합니다.

- **헤더 규격**: 중요 변경 요청에 `X-Idempotency-Key` (UUID v4) 전달.
- **DB Unique 제약**: `(user_id, idempotency_key)` 유니크 제약조건 적용.
- **처리 규칙**:
  - 동일 키 + 동일 요청 본문: 이전 처리 결과 및 상태코드 재현 (`200 OK` 또는 `201 Created`)
  - 동일 키 + 다른 요청 본문: `409 Conflict`
  - 동일 키 + 처리 중: `409 Conflict` 또는 `202 Accepted`

---

## 4. 감사 로그 (Audit Trail) & 개인정보(PII) 마스킹

모든 중요 자산 변동, 결제, 권한 변경 내역은 `audit_logs` 테이블에 보존합니다.

### 1) 개인정보 및 자격증명 마스킹 의무
감사 로그에 평문으로 절대 남겨서는 안 되는 필드:
- 계정 비밀번호, PIN 번호, JWT Secret, 외부 API Secret
- 마스킹 처리: `"pin": "******"`, `"secret": "8qAW...****"`

### 2) 감사 로그 테이블 스키마 (`audit_logs`)
- `id`: BigInteger (PK)
- `user_id`: UUID (Indexed)
- `client_ip`: String(45)
- `user_agent`: String(255)
- `action`: String(50) (예: `USER_LOGIN`, `PAYMENT_CREATE`, `KEY_ROTATE`)
- `request_payload`: JSONB (민감정보 마스킹 완료본)
- `response_summary`: JSONB (민감정보 마스킹 완료본)
- `created_at`: DateTime(timezone=True) (수정/삭제 불가능한 Append-Only)
