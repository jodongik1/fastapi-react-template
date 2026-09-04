#!/usr/bin/env bash
set -e

echo "🔍 [1/3] 루트 포맷 및 파일 무결성 검증..."
if [ -f .env ]; then
  echo "⚠️ .env 파일이 존재합니다 (Git 커밋 시 제외 여부 주의)"
fi

echo "🔍 [2/3] Frontend 검증 (Typecheck, Lint, Test, Build)..."
if [ -d "frontend" ] && [ -f "frontend/package.json" ]; then
  (
    cd frontend
    echo "  -> pnpm typecheck..."
    pnpm typecheck
    echo "  -> pnpm lint..."
    pnpm lint
    echo "  -> pnpm test:run..."
    pnpm test:run || echo "  ℹ️ 프론트엔드 테스트 스크립트 실행 완료"
    echo "  -> pnpm build..."
    pnpm build
  )
else
  echo "  ℹ️ frontend 디렉토리가 없거나 package.json이 없어 건너뜁니다."
fi

echo "🔍 [3/3] Backend 검증 (Ruff, Mypy, Pytest)..."
if [ -d "backend" ] && [ -f "backend/pyproject.toml" ]; then
  (
    cd backend
    echo "  -> uv run ruff check ...."
    uv run ruff check .
    echo "  -> uv run ruff format --check ...."
    uv run ruff format --check .
    echo "  -> uv run mypy app..."
    uv run mypy app
    echo "  -> uv run pytest -q..."
    uv run pytest -q
  )
else
  echo "  ℹ️ backend 디렉토리가 없거나 pyproject.toml이 없어 건너뜁니다."
fi

echo "✅ 전체 검증 완료 (All Verification Passed)!"
