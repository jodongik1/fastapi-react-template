#!/usr/bin/env bash

# 오류 발생 시 스크립트 즉시 중단
set -e

# 1. 인자값(프로젝트명 및 공개 설정) 확인
if [ -z "$1" ]; then
  echo "Error: 프로젝트 이름을 입력해주세요."
  echo "사용법: ./setup_project.sh <새_프로젝트명> [--public|--private]"
  echo "예시: ./setup_project.sh my-project --public"
  exit 1
fi

PROJECT_NAME="$1"
VISIBILITY="${2:---public}" # 기본값: --public (공개)

# VISIBILITY 유효성 검사
if [ "$VISIBILITY" != "--private" ] && [ "$VISIBILITY" != "--public" ] && [ "$VISIBILITY" != "--internal" ]; then
  echo "⚠️  알 수 없는 공개 설정 옵션입니다: $VISIBILITY (기본값인 --public으로 진행합니다.)"
  VISIBILITY="--public"
fi

echo "🚀 '$PROJECT_NAME' ($VISIBILITY) 프로젝트 생성을 시작합니다..."

# 2. 템플릿 기반으로 저장소 생성 및 로컬 클론
echo "📦 GitHub 저장소 생성 및 클론 중..."
gh repo create "$PROJECT_NAME" --template jodongik1/fastapi-react-template "$VISIBILITY" --clone

# 3. 해당 디렉토리로 이동
cd "$PROJECT_NAME"

# 4. 환경 변수 파일 복사
if [ -f .env.example ]; then
  echo "📄 .env 파일 생성 중..."
  cp .env.example .env
else
  echo "⚠️  .env.example 파일이 없어 .env 복사를 건너뜁니다."
fi

# 5. 도커 개발 환경 실행
echo "🐳 Docker 컨테이너 빌드 및 실행 중..."
docker compose up -d --build

echo "✅ '$PROJECT_NAME' 환경 구축이 완료되었습니다!"