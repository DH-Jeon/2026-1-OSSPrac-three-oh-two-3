# 🚀 TEAM 302  
### 2026-1 오픈소스소프트웨어실습 팀 프로젝트

> **삼공이(three-oh-two)** 팀의 Flask 기반 팀 소개 웹 애플리케이션입니다.  
> HTTP 상태 코드 **302 Found**의 의미처럼, 서로 다른 방향에서 출발한 팀원들이 하나의 프로젝트로 모였다는 의미를 담았습니다.

---

## 🧑‍💻 팀 정보

| 항목 | 내용 |
|---|---|
| 팀번호 | 3 |
| 팀명 | 삼공이(three-oh-two) |
| 팀원 | 강지호, 전동현, 조정민 |
| GitHub Repository | https://github.com/CSID-DGU/2026-1-OSSPrac-three-oh-two-3 |
| Docker Hub Repository | https://hub.docker.com/r/jiho0221/team302 |

---

## 📌 프로젝트 소개

**Team 302 웹 애플리케이션**은 Flask를 기반으로 제작한 팀 소개 웹 사이트입니다.

팀의 소개, 팀명 유래, 팀원 정보, 팀원 상세 페이지, Contact 페이지를 제공하며,  
Bootstrap과 CSS, JavaScript를 활용하여 반응형 디자인과 다크모드 기능을 적용했습니다.

Docker를 이용해 누구나 동일한 환경에서 웹 서비스를 실행할 수 있도록 구성했습니다.

---

## 🛠️ 사용 기술

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## ✨ 주요 기능

### 🏠 메인 페이지

- Team 302 소개 문구 제공
- 팀명 `302 Found`의 의미 설명
- 팀 소개 영역과 팀원 카드 표시
- 배경 이미지 및 영상 활용

### 👥 팀원 소개

- 팀원별 카드 UI 제공
- 이름, 역할, 전공, 기술 스택 등 표시
- 팀원 상세 페이지 이동 기능 제공

### 📄 팀원 상세 페이지

- 각 팀원의 개별 정보 확인 가능
- 역할, 기여 내용, 기술 스택 등 상세 정보 제공

### 📞 Contact 페이지

- 팀원별 연락 정보 확인 가능
- GitHub, 이메일 등 외부 링크 제공

### 🌙 다크모드

- JavaScript를 활용한 라이트 모드 / 다크 모드 전환
- `localStorage`를 활용하여 사용자의 모드 선택 유지

### 🎨 디자인 개선

- Bootstrap 5 기반 반응형 레이아웃 적용
- Bootstrap Icons 사용
- 카드형 UI, 네비게이션 바, 애니메이션 효과 적용
- CSS 파일을 분리하여 유지보수성 향상

### 🐳 Docker 배포

- Dockerfile 작성
- docker-compose.yml 작성
- `subject3_2/team.py` 기준으로 Flask 앱 실행
- Docker Hub에 이미지 업로드 가능

---

## 🗂️ 프로젝트 구조

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

            