# React SPA + FastAPI + PostgreSQL Starter Template

> **재현 가능하고 안전한 엔터프라이즈급 풀스택 웹 애플리케이션 보일러플레이트**  
> React 18 (Vite, TypeScript, Tailwind) + Python 3.11 (FastAPI, uv) + PostgreSQL 16 + Docker Compose

---

## 🚀 빠른 시작 (Quick Start)

### 1. 사전 요구사항
- [Docker](https://www.docker.com/) & Docker Compose
- Node.js 20+ (`.node-version`), Python 3.11+ (`.python-version`)

### 2. 환경 변수 복사
```bash
cp .env.example .env
```

### 3. 도커 개발 환경 실행
```bash
# 백그라운드에서 전체 서비스(DB, Backend, Frontend) 실행
docker compose up -d --build

# 실시간 로그 확인
docker compose logs -f
```

- **Frontend**: [http://localhost:5173](http://localhost:5173)
- **Backend Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Backend Healthcheck**: [http://localhost:8000/health](http://localhost:8000/health)

---

## 🛠️ 통합 검증 실행 (Verification)

에이전트 및 로컬 개발 시 단일 명령어로 전체 코드 무결성(린트, 타입체크, 테스트, 빌드)을 검증합니다:

```bash
./scripts/verify.sh
```

---

## 📚 문서 및 상세 설계 (Documentation)

- **[AGENTS.md](AGENTS.md)**: AI 에이전트 작업 헌법 및 단일 진실 공급원(SSOT)
- **[docs/architecture.md](docs/architecture.md)**: 디렉토리 구조, REST API 표준 규격 및 응답 형식
- **[docs/security.md](docs/security.md)**: 비밀번호 해싱(Bcrypt), API Key 암호화(AES-256), 멱등성
- **[docs/profiles/financial-ledger.md](docs/profiles/financial-ledger.md)**: 금융/원장/정밀수치 선택 확장 프로필
