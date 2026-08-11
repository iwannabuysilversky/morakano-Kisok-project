# morakano-Kisok-project

morakano-Kiosk 프로젝트입니다.

```markdown
# 🎙️ AI 음성 인식 키오스크 프로젝트

## 팀원
* **우성: 역할미정** 
* **대호: 역할미정** 
* **승준: 역할미정** 
* **현민: 역할미정** 

## 🛠️ 기술 스택
* **Language:** 미정
* **AI & API:** 미정
* **Environment:**미정
```

---

## Quick Start

---

프로젝트를 로컬 환경에 세팅하는 방법입니다. 아래 명령어들을 순서대로 터미널에 입력해 주세요.
깃은 알아서 까슈

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

# 비활성화
deactivate
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

아직 미정입니다.

```

---

# 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 협업 규칙 (Git Convention)

충돌을 방지하기 위해 다음 규칙을 준수해주세요 !!!!!!!!!!!!!!!!!!!!!!!!!

* **Main 브랜치:** 배포 가능한 안정적인 버전만 유지합니다.(직접 푸시 금지) !!!!!!!!!!!!!!!!!!!!!!!
수정시 팀원과 협의해주세요 !!!!!!!!!!!!!!!!!!!!!!!

* **Feature 브랜치:** 기능 개발 시 `main`에서 브랜치를 분리하여 작업합니다. !!!!!!!!!!!!!!!!!!!!!!!

### * 구체적 방법은 브랜치 작업 설명에 적어놨으니 참고하세요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

* **Pull Request (PR):** 기능 구현 완료 후 PR을 생성하며, 테스트와 팀원의 동의를 진행한 후 Merge 합니다. !!!!!!!!!!!!!!!!!!!!!!!
* **작업 시작 전:** 항상 `git pull origin main`을 통해 로컬을 최신 상태로 유지해 주세요. !!!!!!!!!!!!!!!!!!!!!!!

---

## 🚨 Git 협업 유의사항 및 에러 대처법

### 1. 필수 유의사항
* **작업 시작 전 최신화:** 코드를 짜기 전 무조건 최신 코드를 받아와야(Pull) 과거 코드로 덮어씌워지는 것을 방지할 수 있음.
* **담당 구역 준수:** 자신이 맡은 모듈(파일)만 수정해야 충돌(Conflict)을 원천적으로 예방할 수 있음. 공통 파일(`main.py`, `requirements.txt` 등) 수정 시 디스코드 등에 미리 공유할 것.

### 2. 오류 미리보기

####  내 코드가 안 올라감 (`Updates were rejected`)

* **원인:** 내가 작업하는 동안 다른 팀원이 먼저 코드를 서버(GitHub)에 올린 상태임.
* **대처법:** 서버의 코드를 먼저 내 컴퓨터로 가져와서(Pull) 합친 뒤에 다시 올려야(Push) 함.

```bash
# 1. 서버의 최신 변경사항을 내 컴퓨터로 병합
git pull origin [현재작업중인브랜치명]

# 2. 문제없이 합쳐졌다면 다시 밀어넣기
git push origin [현재작업중인브랜치명]

```

#### Pull을 하려는데 에러가 남 (`Please commit your changes or stash them`)

* **원인:** 내가 코드를 수정하고 아직 저장(Commit)하지 않았는데, 서버에서 최신 코드를 당겨오려다 보니 깃이 내 코드가 날아갈까 봐 차단한 것임.
* **대처법:** 내 변경사항을 잠시 '임시 보관함'에 피신시킨 뒤 코드를 당겨오고 다시 꺼내서 합침.

```bash
git stash              # 1. 내 작업 내역 안전하게 임시 보관 (화면에서 코드가 잠시 사라짐)
git pull origin main   # 2. 서버 최신 코드 안전하게 다운로드
git stash pop          # 3. 보관해둔 내 코드를 다시 꺼내와서 최신 코드 위에 얹기

```

#### 파일 충돌 (`Merge Conflict`) 발생

* **원인:** 팀원과 내가 우연히 '같은 파일의 같은 줄'을 동시에 수정한 경우, 깃이 어떤 코드를 남겨야 할지 몰라 병합을 멈춘 상태임.
* **대처법:** 당황하지 말고 VS Code 에디터에서 해당 파일을 열고 화면에 표시된 충돌 지점(`<<<<<<< HEAD`)에서 남길 코드를 직접 클릭하여 선택(수정)한 후 다시 커밋함.

```bash
# 에디터에서 충돌 코드를 수정한 뒤 터미널에 입력
git add .
git commit -m "fix: 000 파일 충돌 해결"
git push origin [현재작업중인브랜치명]

```

---

### 🚀 Main 브랜치 푸시(Push) 전체 과정

**1. 원본 최신화 (선택이지만 권장함)**

* 다른 팀원이 그새 원본 올렸을수도 있으니까

```bash
git pull origin main

```

**2. 변경된 파일 Add**

* 모든 파일을 add함

```bash
git add .

```

**3. 어떤 작업을 했는지 기록 남기기 (Commit)**

* 어떤 수정사항인지 남기면서 commit함

```bash
git commit -m "여기에 어떤 코드를 수정/추가했는지 설명 작성"

```

**4. 깃허브 서버로 푸시**

* 내 컴퓨터에 저장된 커밋 내역을 실제 깃허브 원격 서버(`origin`)의 `main` 브랜치로 밀어 넣음.

```bash
git push origin main

```

##### 터미널 경로가 프로젝트 최상위 폴더인지 확인한 후에 하도록!!!!!!!!!!!

--- 

###  Feature 브랜치 작업 (명령어 가이드)

**1. 작업 전 `main` 브랜치 최신화**

* 새로운 작업을 시작하기 전에 항상 원본 상태를 최신으로 유지해주세요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
* wkrdjqwj
```bash
git checkout main
git pull origin main

```

**2. Feature 브랜치 생성 및 이동**

* `-b` 옵션을 쓰면 브랜치를 새로 생성함과 동시에 그 feature로 이동함. 예시로 sst-module

```bash
git checkout -b feature/stt-module

```

* *(참고: 터미널 프롬프트에 `(main)`이라고 적혀있던 부분이 `(feature/stt-module)`로 바뀐 것을 반드시 확인)*

**3. 코드 개발 및 커밋**

* 방 안에서 맡은 파일의 코드를 수정하고 기능이 완성되면 커밋을 진행함.

```bash
git add .
git commit -m "feat: 사용자 음성 인식(STT) 기본 로직 구현"
# 만약에 컴을 끄고 자고 싶다! 하면 
git commit -m "wip: stt 모듈 50% 구현 (임시 저장)"

```

**4. 깃허브 서버에 내 작업 브랜치 푸쉬하기**

* 내 컴퓨터에만 있는 작업실을 깃허브 원격 서버로 업로드함.
* 새로 만든 브랜치를 처음 푸시할 때는 서버에 해당 브랜치가 없으므로 `-u` (또는 `--set-upstream`) 옵션을 붙여서 경로를 연결해야함!!!!!!!!!!!!!!!!!!!!!!!

```bash
git push -u origin feature/stt-module
# 만약 컴을 끄고 자고싶다 하면 
git push origin [현재내브랜치명]

```

**5. 깃허브 웹에서 PR(Pull Request) 생성 및 병합 (Merge)**

* 프로젝트 깃허브 접속(https://github.com/iwannabuysilversky/morakano-Kisok-project)
* 방금 푸시를 했기 때문에 페이지 상단에 초록색 버튼으로 **`Compare & pull request`** 라는 버튼 클릭
* 어떤 작업을 했는지 상세히 적고 PR을 생성함. 어떤 작업을 했는지 리뷰 제대로 할것
* 다른 팀원들이 코드를 확인하고 승인(Approve)하면, 리더가 **`Merge pull request`** 버튼을 눌러 원본 main 브랜치에 최종적 merge함 인데 2명 이상이 하면 되도록 바꿀 예정입니다

**6. 작업 완료 후 로컬 최신화**

* 내 코드가 main에 성공적으로 합쳐졌다면, 다시 내 컴퓨터로 돌아와서 최신화된 main을 pull함

```bash
git checkout main
git pull origin main

```
