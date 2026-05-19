from flask import Flask, render_template, abort

app = Flask(__name__)

# ============================================================
# 팀 메타 정보
# ============================================================
TEAM_INFO = {
    "name": "Team 302",
    "tagline": "Data meets the Web",
    "description": (
        "통계 분석, 머신러닝, 웹 개발 — 서로 다른 관심사를 가진 세 사람이 "
        "오픈소스소프트웨어실습이라는 한 강의실로 리다이렉트되어 만났습니다. "
        "같은 전공이든 다른 전공이든, 한 학기 동안 같은 페이지에서 어우러지는 팀입니다."
    ),
    "stats": [
        {"value": "3",  "label": "Members"},
        {"value": "3",  "label": "Roles"},
        {"value": "8+", "label": "Projects"},
        {"value": "10+", "label": "Tech Stack"},
    ],
    "name_origin": {
        "code": "302",
        "status": "Found",
        "headline": "302 Found — 서로 다른 길에서, 같은 강의실로",
        "summary": (
            "HTTP 302는 요청을 다른 자원으로 잠시 안내해주는 응답입니다. "
            "데이터 분석, 머신러닝, 프론트엔드 — 서로 다른 관심사를 가진 세 사람이 "
            "오픈소스소프트웨어실습이라는 한 강의실로 리다이렉트되어 만났습니다. "
            "각자의 본래 길은 그대로 유지한 채, 한 학기 동안 같은 페이지에서 어우러지는 팀, 그게 Team 302입니다."
        ),
        "points": [
            {
                "icon": "bi-signpost-split",
                "title": "서로 다른 관심사",
                "desc": "통계 데이터의 인사이트, 머신러닝 모델링, 프론트엔드 웹 — 세 사람의 시선이 향한 방향은 각자 달랐습니다."
            },
            {
                "icon": "bi-arrow-right-circle",
                "title": "같은 곳으로 리다이렉트",
                "desc": "OSS 실습이라는 하나의 Location으로 안내되어, 한 학기 동안 같은 코드베이스 위에서 만났습니다."
            },
            {
                "icon": "bi-geo-alt-fill",
                "title": "서로의 Location",
                "desc": "302 응답이 Location 헤더로 다음 목적지를 알려주듯, 우리는 서로에게 새로운 길을 안내합니다. 통계의 인사이트는 모델로, 모델의 결과는 사용자에게."
            }
        ]
    }
}

# ============================================================
# 팀원 데이터 (이력서 기반)
# ============================================================
TEAM_MEMBERS = [
    {
        "id": 1,
        "name": "강지호",
        "english_name": "Jiho Kang",
        "role": "Data Analyst",
        "tag": "Statistics · SPSS · R",
        "intro": "통계 데이터를 다루며 인사이트를 발견하는 것을 좋아합니다.",
        "detail_intro": (
            "통계학을 주전공으로 하며, 소프트웨어·AI를 연계전공으로 학습 중인 22학번 학생입니다. "
            "SPSS, SAS, R 등 통계 도구에 익숙하며, 가설 검정과 시각화를 통한 데이터 인사이트 도출에 강점이 있습니다. "
            "실제 국가별 GDP·행복지수 데이터를 활용한 분석 프로젝트를 수행했습니다."
        ),
        "education": {
            "university": "동국대학교",
            "major": "통계학과 (주전공)",
            "sub_major": "소프트웨어·AI (연계전공)",
            "year": "22학번 · 3학년"
        },
        "skills": [
            {"name": "R", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg"},
            {"name": "Python", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
            {"name": "Java", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"},
            {"name": "Jupyter", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg"},
            {"name": "VS Code", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"},
            {"name": "Eclipse", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/eclipse/eclipse-original.svg"}
        ],
        "tools": ["SPSS (중급)", "SAS (중급)", "R Studio"],
        "projects": [
            {
                "title": "행복은 돈과 비례하는가에 대한 분석",
                "desc": "SPSS를 활용한 통계 기법으로 국가별 GDP와 행복지수 데이터를 결합·정리. 다양한 시각화 및 가설 검정 기반 데이터 분석 진행",
                "tech": ["SPSS", "통계 분석", "가설 검정"]
            }
        ],
        "certificates": [],
        "contribution": "데이터 분석 및 통계 검증, 사용자 데이터 수집 설계, 가설 검정 기반 인사이트 도출",
        "contribution_percent": 33,
        "github": "https://github.com/Jiho0221",
        "email": "wlgh02211@gmail.com",
        "phone": "010-7440-2310",
        "image": "https://i.pravatar.cc/400?img=33",
        "color": "#0f766e",
        "color_dark": "#134e4a"
    },
    {
        "id": 2,
        "name": "전동현",
        "english_name": "Donghyun Jeon",
        "role": "ML Engineer",
        "tag": "ML · Python · Data Science",
        "intro": "머신러닝 모델 설계와 데이터 분석을 담당합니다.",
        "detail_intro": (
            "통계학을 주전공으로, 소프트웨어·AI를 복수전공으로 학습 중인 동국대학교 3학년 학생입니다. "
            "Random Forest, GBM, XGBoost 등 다양한 머신러닝 모델 경험을 보유하고 있으며, "
            "Kaggle 데이터, 의료 데이터, 공공 데이터 등 다양한 도메인의 실전 프로젝트를 수행했습니다. "
            "데이터 전처리부터 모델링, 성능 비교까지 전 과정을 담당할 수 있습니다."
        ),
        "education": {
            "university": "동국대학교",
            "major": "통계학과 (주전공)",
            "sub_major": "소프트웨어·AI (복수전공)",
            "year": "3학년 재학 중"
        },
        "skills": [
            {"name": "Python", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
            {"name": "R", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg"},
            {"name": "Pandas", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"},
            {"name": "NumPy", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg"},
            {"name": "scikit-learn", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg"},
            {"name": "Java", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"},
            {"name": "Git", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"},
            {"name": "IntelliJ", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/intellij/intellij-original.svg"}
        ],
        "tools": ["Decision Tree", "Random Forest", "K-Means", "PCA", "GBM", "XGBoost", "Seaborn", "Matplotlib"],
        "projects": [
            {
                "title": "타이타닉 탑승자 생존 여부 예측",
                "desc": "Kaggle 데이터를 활용한 생존 예측 모델. 결측치 처리, 범주형 인코딩 후 Random Forest와 GBM 성능 비교",
                "tech": ["Python", "Pandas", "Scikit-learn", "Seaborn"]
            },
            {
                "title": "당뇨병 발병 여부 예측",
                "desc": "의료 데이터 기반 분류 모델 개발. 정규화 및 변수 중요도 분석 후 GBM 적용",
                "tech": ["Python", "Random Forest", "GBM"]
            },
            {
                "title": "일별 따릉이 대여량 예측",
                "desc": "서울시 공공데이터 기반 회귀 모델. 기온, 강수량, 요일 등 특성 활용",
                "tech": ["Python", "회귀 모델", "Pandas"]
            },
            {
                "title": "고객 이탈 여부 예측",
                "desc": "Kaggle 데이터로 Churn 예측 모델 구축. Random Forest와 XGBoost 성능 비교",
                "tech": ["Python", "Random Forest", "XGBoost"]
            }
        ],
        "certificates": [
            {"name": "컴퓨터활용능력 1급", "issuer": "대한상공회의소", "date": "2024.10"},
            {"name": "ADsP (데이터분석 준전문가)", "issuer": "한국데이터산업진흥원", "date": "2026.03"}
        ],
        "contribution": "백엔드 ML 모델 설계 및 학습, 데이터 전처리 파이프라인 구축, API 연동 로직 구현",
        "contribution_percent": 34,
        "github": "https://github.com/DH-Jeon",
        "email": "2022110488@naver.com",
        "phone": "010-6748-0213",
        "image": "https://i.pravatar.cc/400?img=12",
        "color": "#ea580c",
        "color_dark": "#9a3412"
    },
    {
        "id": 3,
        "name": "조정민",
        "english_name": "Jeongmin Cho",
        "role": "Frontend Developer",
        "tag": "HTML · CSS · JavaScript",
        "intro": "프론트엔드 웹 개발에 관심이 많은 정보통신공학도입니다.",
        "detail_intro": (
            "정보통신공학을 전공하는 동국대학교 3학년 학생으로, 웹 개발 분야에 깊은 관심을 가지고 있습니다. "
            "HTML, CSS, JavaScript 등 웹 기초 기술을 학습하며 VS Code 환경에서 다양한 실습을 진행해 왔습니다. "
            "오픈소스 소프트웨어 실습 수업을 통해 Git 기반 협업과 프론트엔드 개발 역량을 쌓는 것을 목표로 하고 있습니다."
        ),
        "education": {
            "university": "동국대학교",
            "major": "정보통신공학과",
            "sub_major": "프론트엔드 웹 개발 (관심 분야)",
            "year": "2022 - 현재"
        },
        "skills": [
            {"name": "HTML5", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"},
            {"name": "CSS3", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"},
            {"name": "JavaScript", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
            {"name": "React", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"},
            {"name": "Python", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
            {"name": "VS Code", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"},
            {"name": "Git", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"},
            {"name": "GitHub", "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"}
        ],
        "tools": ["JSX", "정보통신프로그래밍", "프로그래밍기초와실습", "ICT와소프트웨어"],
        "projects": [
            {
                "title": "Flask 기반 팀 소개 웹 페이지",
                "desc": "Flask 라우팅과 Jinja2 템플릿을 활용해 다중 페이지 구조의 팀 소개 사이트 구축",
                "tech": ["Flask", "Jinja2", "Bootstrap"]
            },
            {
                "title": "Git 협업 워크플로우 실습",
                "desc": "GitHub 기반 브랜치, 커밋, PR 워크플로우 학습 및 팀 협업 실습",
                "tech": ["Git", "GitHub", "Branch"]
            }
        ],
        "certificates": [],
        "contribution": "프론트엔드 UI/UX 설계, HTML/CSS 페이지 구현, Flask 템플릿 연동, 반응형 디자인 적용",
        "contribution_percent": 33,
        "github": "https://github.com/youngb0",
        "email": "jm11n@naver.com",
        "phone": "010-7501-8059",
        "image": "https://i.pravatar.cc/400?img=68",
        "color": "#e11d48",
        "color_dark": "#9f1239"
    }
]


# ============================================================
# 라우팅
# ============================================================
@app.route("/")
def index():
    return render_template("index.html",
                           team=TEAM_INFO,
                           members=TEAM_MEMBERS,
                           active_page="home")


@app.route("/members/<int:member_id>")
def member_detail(member_id):
    member = next((m for m in TEAM_MEMBERS if m["id"] == member_id), None)
    if member is None:
        abort(404)
    return render_template("member_detail.html",
                           member=member,
                           members=TEAM_MEMBERS,
                           active_page="members")


@app.route("/contact")
def contact():
    return render_template("contact.html",
                           team=TEAM_INFO,
                           members=TEAM_MEMBERS,
                           active_page="contact")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
