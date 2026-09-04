# 금융 데이터 정밀도, 원장 보존 및 감사 로그 프로필 (docs/profiles/financial-ledger.md)

> ℹ️ **안내**: 본 문서는 **금융, 가상자산, 정밀 결제 또는 거래소 연동 기능이 활성화된 프로젝트**에만 선택적으로 적용되는 확장 도메인 규칙입니다. 일반 CRUD/웹 서비스 프로젝트에는 강제되지 않습니다.

---

## 1. 정밀 수치 데이터 타입 표준
- **금액 / 가격**: `Numeric(18, 4)` 또는 Python `Decimal` (부동소수점 Float 절대 금지)
- **수량**: `Numeric(18, 8)` 또는 Python `Decimal` (소수점 거래 지원)
- **통화 코드**: 금액 관련 테이블에는 `currency: String(3)` (KRW, USD 등) 필수 선언

## 2. 거래 원장 보존 원칙 (Soft Delete)
- 보존 대상 원장(주문, 결제, 체결)을 참조하는 외래키에는 `ON DELETE CASCADE`를 사용하지 않습니다.
- 탈퇴 시 회원은 `is_active=False`로 비활성화하고, 금융 원장 및 거래 이력은 법적 보존 의무를 위해 보존합니다.

## 3. 엄격한 멱등성 및 원장 분리
- 결제/주문 API 요청 시 헤더에 `X-Idempotency-Key` (UUID)를 전달받고, `(user_id, idempotency_key)` 유니크 제약조건을 통해 중복 처리를 원천 차단합니다.
- 동일 키 + 동일 요청 ➡️ 이전 응답 결과 재현 (`200 OK` / `201 Created`)
- 동일 키 + 다른 요청 ➡️ `409 Conflict` 반환
