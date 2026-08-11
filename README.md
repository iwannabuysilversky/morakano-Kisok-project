# morakano-Kisok-project
morakano-Kiosk 프로젝트입니다.

```markdown
# 🎙️ AI 음성 인식 키오스크 프로젝트

## 팀원
* **조우성: 역할 미정** 
* **원대호: 역할 미정** 
* **이승준: 역할 미정** 
* **양현민: 역할 미정** 

## 🛠️ 기술 스택
* **Language:** 미정
* **AI & API:** 미정
* **Environment:**미정
```

---

## Quick Start

---

프로젝트를 로컬 환경에 세팅하는 방법입니다. 아래 명령어들을 순서대로 터미널에 입력해 주세요.

### 1. 저장소 클론 및 폴더 이동
```bash
git clone https://github.com/iwannabuysilversky/morakano-Kisok-project.git
cd morakano-Kisok-project

```

### 2. 가상환경(venv) 생성 및 활성화

```bash
# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. 필수 패키지 설치

```bash
pip install -r requirements.txt

```

### 4. 환경 변수(.env) 설정

루트 디렉토리에 있는 `.env.example` 파일을 복사하여 `.env` 파일을 생성하고, 발급받은 API 키를 입력합니다.   
`.env` 파일은 절대 깃허브에 커밋(푸시)하지 마세요!

```bash
# .env 파일 내용 예시
OPENAI_API_KEY="sk-여기에-발급받은-키를-입력하세요"

```

---

# 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 5 협업 규칙 (Git Convention)

충돌을 방지하기 위해 다음 규칙을 준수해주세요 !!!!!!!!!!!!!!!!!!!!!!!!!

* **Main 브랜치:** 배포 가능한 안정적인 버전만 유지합니다.(직접 푸시 금지) !!!!!!!!!!!!!!!!!!!!!!!
수정시 팀원과 협의해주세요 !!!!!!!!!!!!!!!!!!!!!!!

* **Feature 브랜치:** 기능 개발 시 `main`에서 브랜치를 분리하여 작업합니다. !!!!!!!!!!!!!!!!!!!!!!!
* 예시: `feature/stt-module`, `feature/prompt-test`

* **Pull Request (PR):** 기능 구현 완료 후 PR을 생성하며, 테스트와 팀원의 동의를 진행한 후 Merge 합니다. !!!!!!!!!!!!!!!!!!!!!!!
* **작업 시작 전:** 항상 `git pull origin main`을 통해 로컬을 최신 상태로 유지해 주세요. !!!!!!!!!!!!!!!!!!!!!!!
