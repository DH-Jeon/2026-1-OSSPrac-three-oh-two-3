# 🧭 Team 302

<div align="center">

## 삼공이 `three-oh-two`

**Flask 기반 팀 소개 웹사이트**

서로 다른 방향에서 출발한 세 명의 팀원이  
하나의 프로젝트 안에서 만나 완성한 Team 302 웹 페이지입니다.

<br>

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=flat-square&logo=flask&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-Template-B41717?style=flat-square&logo=jinja&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Markup-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Style-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Interaction-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=flat-square&logo=docker&logoColor=white)

</div>

---

## 🌐 About Team 302

**Team 302**는 팀 소개를 주제로 제작한 Flask 웹 애플리케이션입니다.

팀명 **302**는 HTTP 상태 코드 `302 Found`에서 가져왔습니다.  
`302 Found`가 사용자를 새로운 위치로 안내하듯,  
Team 302는 각자의 관심사와 역할을 하나의 프로젝트 안에서 연결한다는 의미를 담고 있습니다.

이 웹사이트에서는 팀 소개, 팀원 정보, 팀원 상세 페이지, Contact 페이지를 확인할 수 있으며,  
다크모드와 반응형 디자인을 적용하여 더 편리하게 페이지를 둘러볼 수 있도록 구성했습니다.

---

## ✨ Main Point

Team 302 웹사이트는 단순한 팀 소개 페이지가 아니라,  
팀의 이름과 개성을 시각적으로 보여주는 작은 포트폴리오형 웹 페이지입니다.

- 팀명 `302 Found`의 의미를 활용한 소개 스토리
- 팀원별 카드와 상세 페이지 구성
- Contact 페이지를 통한 팀원 정보 확인
- Bootstrap 기반 반응형 레이아웃
- JavaScript를 활용한 다크모드 기능
- Docker 기반 실행 환경 제공

---

## 🖥️ Page Preview

| Page | Description |
|---|---|
| Home | Team 302의 메인 소개 페이지 |
| Team Story | `302 Found`를 바탕으로 한 팀명 소개 |
| Members | 팀원 카드를 통해 각 팀원 정보 확인 |
| Member Detail | 팀원별 상세 정보와 역할 확인 |
| Contact | 팀원 연락 정보 확인 |
| Input / Result | Flask 입력 및 결과 페이지 |

---

## 🧩 Features

### 🏠 Home

Team 302의 첫 화면입니다.  
팀 소개 문구, 팀명 의미, 팀원 카드, 배경 이미지 및 영상 요소를 통해 팀의 분위기를 보여줍니다.

### 👥 Members

팀원 정보를 카드 형태로 제공합니다.  
각 팀원의 이름, 역할, 전공, 기술 스택 등을 한눈에 확인할 수 있습니다.

### 📄 Member Detail

팀원 카드를 클릭하면 상세 페이지로 이동합니다.  
각 팀원의 개별 소개, 역할, 프로젝트 내 기여 내용을 확인할 수 있습니다.

### 📞 Contact

팀원별 연락 정보를 모아둔 페이지입니다.  
이메일, GitHub 등 외부 링크 정보를 확인할 수 있습니다.

### 🌙 Dark Mode

JavaScript와 `localStorage`를 활용해  
사용자가 라이트 모드와 다크 모드를 전환할 수 있도록 구현했습니다.

### 🎨 Responsive Design

Bootstrap과 커스텀 CSS를 활용하여  
PC와 다양한 화면 크기에서 자연스럽게 보이도록 구성했습니다.

---

## 🛠️ Tech Stack

| Category | Stack |
|---|---|
| Backend | Python, Flask |
| Template | Jinja2 |
| Frontend | HTML5, CSS3, JavaScript |
| UI | Bootstrap 5, Bootstrap Icons |
| Server | uWSGI, Nginx |
| Container | Docker, Docker Compose |

---

## 📁 Project Structure

```text
Team Project/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── README.md
├── subject3_1/
│   ├── ex4.py
│   └── templates/
│       ├── input.html
│       └── result.html
└── subject3_2/
    ├── team.py
    ├── uwsgi.ini
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   ├── contact.html
    │   ├── input.html
    │   ├── result.html
    │   └── member_detail.html
    └── static/
        ├── css/
        │   └── style.css
        ├── js/
        │   └── theme.js
        ├── images/
        │   ├── dubai_poster.jpg
        │   ├── member1.svg
        │   ├── member2.svg
        │   └── member3.svg
        └── videos/
            └── dubai.mp4
```

---

## 🚦 실행 기준

이 프로젝트의 실제 Flask 실행 파일은 다음 위치에 있습니다.

```text
subject3_2/team.py
```

`team.py` 내부에는 Flask 앱 객체가 다음과 같이 정의되어 있습니다.

```python
app = Flask(__name__)
```

Docker 환경에서도 이 파일을 기준으로 실행되도록 구성되어 있습니다.

---

## 🚀 How to Run

Team 302 웹사이트는 로컬 환경 또는 Docker 환경에서 실행할 수 있습니다.

---

### 1. 프로젝트 내려받기

```bash
git clone https://github.com/CSID-DGU/2026-1-OSSPrac-three-oh-two-3.git
cd 2026-1-OSSPrac-three-oh-two-3
```

프로젝트 안에 `Team Project` 폴더가 있는 경우:

```bash
cd "Team Project"
```

---

### 2. Docker로 실행하기

프로젝트 최상위 폴더에서 아래 명령어를 실행합니다.

```bash
docker compose up --build -d
```

구버전 Docker Compose를 사용하는 경우:

```bash
docker-compose up --build -d
```

---

### 3. 웹사이트 접속하기

브라우저에서 아래 주소로 접속합니다.

```text
http://localhost:8000
```

---

### 4. 실행 종료하기

```bash
docker compose down
```

구버전 Docker Compose를 사용하는 경우:

```bash
docker-compose down
```

---

## 🐳 Docker Hub로 바로 실행하기

Docker Hub에 업로드된 이미지를 바로 실행할 수도 있습니다.

```bash
docker pull jiho0221/team302:latest
docker run -d -p 8000:80 --name team302-web jiho0221/team302:latest
```

브라우저에서 아래 주소로 접속합니다.

```text
http://localhost:8000
```

컨테이너를 중지하려면 아래 명령어를 실행합니다.

```bash
docker stop team302-web
docker rm team302-web
```

## ⚙️ Docker Configuration

<details>
<summary>Dockerfile</summary>

```dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.12

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY subject3_2/ /app/

ENV STATIC_PATH=/app/static
EXPOSE 80
```

</details>

<details>
<summary>docker-compose.yml</summary>

```yaml
services:
  app:
    build: .
    image: jiho0221/team302:latest
    container_name: team302-web
    ports:
      - "8000:80"
    restart: unless-stopped
```

</details>

<details>
<summary>uwsgi.ini</summary>

```ini
[uwsgi]
module = team
callable = app
enable-threads = true
```

</details>

---

## 🔗 Routes

| Method | Route | Page |
|---|---|---|
| GET | `/` | Main Page |
| GET | `/contact` | Contact Page |
| GET | `/members/<id>` | Member Detail Page |
| GET | `/input` | Input Page |
| POST | `/result` | Result Page |

---

## 🧑‍💻 Team Members

| Name | Role |
|---|---|
| 강지호 | Docker 환경 구성, Flask 실행 환경 설정, README 작성 |
| 전동현 | 팀 소개 콘텐츠 구성, HTML 페이지 구성 |
| 조정민 | Contact 페이지 구성, CSS 및 JavaScript 기능 개선 |

---

## 🔗 Links

### GitHub Repository

```text
https://github.com/CSID-DGU/2026-1-OSSPrac-three-oh-two-3
```

### Docker Hub Repository

```text
https://hub.docker.com/r/jiho0221/team302
```

---

<div align="center">

### Team 302

`302 Found`  
서로 다른 길에서 만나 하나의 페이지를 완성하다.

<br>

2026-1 오픈소스소프트웨어실습  
Dongguk University

</div>