# React SPA + FastAPI + PostgreSQL 스타터 템플릿 개발 가이드 (AGENTS.md)

이 문서는 **React SPA + FastAPI + PostgreSQL (Docker)** 프로젝트의 기술 스택 단일 진실 공급원(SSOT), AI 에이전트 작업 제약 조건, 검증 절차 및 완료 기준을 정의합니다.
모든 AI 에이전트는 본 저장소 내 작업 시 본 헌법의 규칙을 최우선으로 준수해야 합니다.

---

## 1. 확정 기술 스택 및 단일 진실 공급원 (SSOT)

도구 및 라이브러리 버전의 단일 진실 공급원은 **각 manifest 파일과 lockfile**입니다. 본 문서의 설명과 실제 lockfile이 충돌할 경우 **lockfile 및 매니페스트를 절대 우선**합니다.

### 1) Frontend Stack
- **Runtime**: Node.js (`.node-version` 고정)
- **Package Manager**: `pnpm` (`package.json#packageManager` 및 `pnpm-lock.yaml`)
- **Framework**: React 18 / Vite
- **Styling**: Tailwind CSS (v3 기준), `clsx`, `tailwind-merge`, `class-variance-authority` (cva)
- **Language**: TypeScript (엄격한 Strict 모드, `noImplicitAny: true`)
- **State / Cache**: Zustand (Auth/UI 상태), TanStack Query (v5, 서버 데이터 캐싱)
- **Routing**: `react-router-dom` (v6+, 메뉴/화면별 중첩 라우팅 및 `DashboardLayout` 공통 컴포넌트 재사용)
- **UI Components**: `lucide-react`, `sonner` (Toast 알림), `react-hook-form`, `zod`
- **HTTP Client**: Axios (`retryAfterRefresh` 메타데이터 기반)
- **Lint / Format**: ESLint (Flat Config), Prettier

### 2) Backend Stack
- **Runtime**: Python 3.11 (`.python-version` 고정)
- **Package Manager**: `uv` (Manifest: `pyproject.toml`, Lockfile: `uv.lock`)
- **Framework**: FastAPI (비동기 I/O, Pydantic v2 기반 요청/응답 검증)
- **Security / Auth**: `passlib[bcrypt]` (비밀번호 해싱), `PyJWT` (JWT 토큰), `cryptography` (AES-256-GCM), `httpx` (비동기 통신)
- **ORM / DB**: SQLAlchemy 2.0 (비동기 `asyncpg`), Alembic
- **Quality Tools**: Ruff (Lint & Format), Mypy (Strict Type Check), Pytest

### 3) Database & Infra
- **Primary DB**: PostgreSQL 16 (UTF-8 인코딩)
- **Dev Environment**: Docker & Docker Compose (`docker-compose.yml`)

---

## 2. 상세 설계 및 도메인 확장 문서 참조 (상대경로)

- **아키텍처 및 API 표준**: [docs/architecture.md](docs/architecture.md) (디렉토리 구조, REST 에러 규격, UTC 날짜)
- **보안 & 암호화 표준**: [docs/security.md](docs/security.md) (Bcrypt 해싱, AES-256-GCM, 401 Silent Refresh 원칙)
- **도메인 확장 프로필 (선택 적용)**:
  - 금융/원장/정밀수치: [docs/profiles/financial-ledger.md](docs/profiles/financial-ledger.md) (결제 및 금융 도메인 활성화 시 준수)
  - KIS 증권 연동 가이드: [docs/profiles/kis-broker.md](docs/profiles/kis-broker.md) (한국투자증권 API 연동 시 tr_id, 토큰 캐싱, 엔드포인트 준수)

---

## 3. 도커 개발 환경 및 핫 리로딩 규칙 (Dev Environment)

1. **호스트-컨테이너 격리 및 HMR**:
   - 프론트엔드: `./frontend:/app` (`node_modules`는 익명/Named 볼륨으로 호스트와 격리)
   - 백엔드: `./backend:/app` (`.venv`, `__pycache__` 격리)
   - HMR 폴링: `CHOKIDAR_USEPOLLING=true` 환경변수 기반으로 동작
2. **컨테이너 빌드/재시작 가이드**:
   - 단순 소스 코드(TS, TSX, PY, CSS) 수정 시에는 재빌드/재시작 금지 (HMR과 Uvicorn `--reload` 활용)
   - **의존성 변경 시 해당 서비스만 빌드**:
     - 프론트 패키지 변경 (`package.json`, `pnpm-lock.yaml`): `docker compose build frontend && docker compose up -d frontend`
     - 백엔드 패키지 변경 (`pyproject.toml`, `uv.lock`): `docker compose build backend && docker compose up -d backend`

---

## 4. UI/UX 디자인 시스템 및 인터랙션 원칙

- **디자인 룩앤필**: 모던 엔터프라이즈 대시보드 스타일 (Dark `bg-slate-900` / Light `bg-slate-50`, Blue Accent `#3874ff`)
- **타이포그래피**: `Inter`, `Pretendard`, sans-serif (시스템 폰트 폴백 보장)
- **임의 픽셀(Arbitrary values) 지양**: `w-[137px]` 대신 Tailwind 표준 스페이싱 토큰(`p-4`, `h-10`, `text-sm`, `rounded-xl`)을 엄격히 사용.
- **컴포넌트 변형 처리**: 버튼, 뱃지 등 UI 컴포넌트는 `cva`와 `cn(clsx, twMerge)` 유틸리티를 사용하여 클래스 충돌 방지 및 체계적인 Variant 관리.
- **깜빡임 없는 UI**: TanStack Query의 `placeholderData: keepPreviousData` 활용
- **3대 상태(State) 필수 구현**:
  - 로딩 중: 실제 레이아웃 크기를 유지하는 `Skeleton` 로더 노출 (`animate-pulse bg-slate-200 dark:bg-slate-700 rounded`)
  - 데이터 없음: 친절한 안내 메시지가 포함된 `Empty State` UI (유효한 다음 액션이 있을 때만 버튼 노출)
  - 에러 발생: 재시도 버튼이 포함된 `Error Alert`
- **폼 유효성 검사 & 피드백**:
  - `react-hook-form` + `zod` 기반 클라이언트 검증.
  - 에러 발생 시 입력창 테두리 `border-rose-500 focus:ring-rose-500/20` 강조 및 하단 에러 문구(`text-rose-500 text-xs mt-1`) 출력.
  - 비동기 작업 결과 피드백은 브라우저 기본 `alert` 대신 `sonner` 토스트 알림 활용.
- **반응형(Mobile-First) & 터치 접근성**:
  - 모바일에서는 사이드바가 슬라이드 오버레이 Drawer로 전환되며, 클릭 요소는 최소 `44x44px` 터치 타겟 확보.
- **웹 접근성(a11y)**: 텍스트 없는 아이콘 버튼에 `aria-label` 필수, 모달은 `role="dialog"`, `aria-modal="true"`, 포커스 트랩 및 ESC 닫기 지원 (입력 중인 모달은 배경 클릭 닫기 금지).

---

## 5. 데이터베이스 설계 및 표준화 규칙

- **마이그레이션 필수**: 모든 테이블 스키마 변경은 직접 SQL 실행 금지, 반드시 Alembic 마이그레이션 파일 작성.
- **네이밍 컨벤션**: 테이블명과 컬럼명은 snake_case, 외래키는 `{table_singular}_id` 명시.
- **시간대 처리**: 모든 일시 컬럼은 `DateTime(timezone=True)`로 선언하고 UTC 기준으로 저장.
- **DDL 코멘트**: 모든 SQLAlchemy 모델과 컬럼에 `comment` 메타데이터 작성 필수.
- **불변조건**: 금융/결제 도메인이 아닌 일반 엔티티는 도메인 요구사항에 따라 적절한 ON DELETE 정책을 적용.

---

## 6. AI 에이전트 작업 제약 사항 (Strict Guardrails)

1. **테스트 코드 보호**: 테스트 통과만을 목적으로 테스트를 삭제하거나 assertion을 약화하지 않는다. 요구사항 변경으로 테스트 수정이 필요한 경우, 변경 이유와 기존 동작 차이를 사용자에게 보고한다.
2. **에이전트 권한 경계 (안전 수칙)**:
   - 사용자의 기존 변경사항을 임의로 덮어쓰거나 되돌리지 않는다.
   - 요청받은 범위 밖의 파일을 불필요하게 대규모 리팩토링하지 않는다.
   - 데이터 삭제, 마이그레이션 다운그레이드, DB 초기화 전에는 사용자 승인을 요청한다.
   - `.env` 등 비밀 파일의 내용을 화면에 출력하거나 로그에 남기지 않는다.
3. **단일 책임 원칙 (SRP)**: 파일 줄 수로 억지로 쪼개지 말고, 비즈니스 로직(Hook)과 UI(View)가 혼재되면 Container/Presentational 패턴으로 분리 검토한다.
4. **부작용 있는 요청 자동 재시도 금지**: 401 토큰 갱신 시 `retryAfterRefresh === false`인 변경/결제 요청은 자동 재전송하지 않는다.

---

## 7. 검증 절차 및 완료 기준 (Definition of Done)

코드를 수정한 후, 에이전트는 **저장소 루트에서 단일 검증 스크립트(`scripts/verify.sh`)**를 실행하거나 서브셸 형태로 변경 범위에 맞는 검증을 수행해야 합니다.

### 1) 단일 통합 검증 실행 (가장 권장)
```bash
./scripts/verify.sh
```

### 2) 개별 서브셸 검증 명령 (디렉토리 중첩 방지 서브셸 괄호 필수)
```bash
# 프론트엔드 검증
(cd frontend && pnpm typecheck && pnpm lint && pnpm test:run && pnpm build)

# 백엔드 검증
(cd backend && uv run ruff check . && uv run ruff format --check . && uv run mypy app && uv run pytest -q)
```

### 3) 완료 보고 규칙
- 본인이 수정한 코드로 인해 발생한 검증 실패는 반드시 해결 후 보고해야 합니다.
- 기존의 환경 문제나 권한 이슈로 특정 검증을 실행하지 못했다면, 최종 보고 시 **어떤 검증을 왜 실행하지 못했는지 명시적**으로 보고해야 합니다.

---

## 8. Git 형상 관리 및 커밋 컨벤션 (Git Workflow)

1. **사용자 요청 기반 커밋 원칙**: 사용자가 명시적으로 커밋/푸시를 요청한 경우에만 `git commit`을 수행한다.
2. **커밋 메시지 표준 (Conventional Commits)**:
   - `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:` 접두사 사용.
   - 명령문 형태의 명확한 설명 작성 (예: `feat: 사용자 인증 토큰 갱신 로직 구현`)
3. **보안 커밋 가드레일**:
   - 커밋 전 `git status --short` 및 `git diff --cached`를 통해 `.env`나 민감 자격증명이 스테이징되지 않았는지 필수 확인.
   - 빌드 아티팩트(`dist/`, `__pycache__/`, `.venv/`, `node_modules/`) 커밋 절대 금지.
