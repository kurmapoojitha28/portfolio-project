from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Personal Portfolio")
BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

SKILLS = [
    "Python", "FastAPI", "HTML5", "CSS3", "SQL", "MySQL",
    "Git & GitHub", "Jinja2", "REST APIs"
]

PROJECTS = [
    {
        "title": "Bank Management System",
        "description": "A Python application for managing customer accounts, deposits, withdrawals, and balance inquiries.",
        "tech": ["Python", "MySQL"],
        "link": "https://github.com/",
    },
    {
        "title": "Personal Portfolio",
        "description": "A server-rendered portfolio featuring Jinja2 templates and persistent theme preferences.",
        "tech": ["Python", "FastAPI", "HTML", "CSS"],
        "link": "https://github.com/",
    },
    {
        "title": "Product Catalog",
        "description": "A simple product listing application using FastAPI, forms, and a database.",
        "tech": ["Python", "FastAPI", "SQL"],
        "link": "https://github.com/",
    },
]


@app.get("/")
async def home(request: Request, tech: str | None = None, sent: str | None = None):
    theme = request.cookies.get("theme", "light")
    projects = PROJECTS
    if tech:
        projects = [
            project for project in PROJECTS
            if any(tech.lower() == item.lower() for item in project["tech"])
        ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "theme": theme,
            "year": datetime.now().year,
            "skills": SKILLS,
            "projects": projects,
            "tech_filter": tech or "",
            "sent": sent,
        },
    )


@app.post("/set-theme")
async def set_theme(request: Request):
    current_theme = request.cookies.get("theme", "light")
    new_theme = "dark" if current_theme == "light" else "light"

    # Keep the user on the page where the theme button was submitted.
    referrer = request.headers.get("referer", "/")
    response = RedirectResponse(url=referrer, status_code=303)
    response.set_cookie(
        key="theme",
        value=new_theme,
        max_age=2592000,  # 30 days
        httponly=True,
        samesite="lax",
        path="/",
    )
    return response


@app.post("/contact")
async def contact(
    name: str = Form(..., min_length=2, max_length=80),
    email: str = Form(..., min_length=5, max_length=120),
    message: str = Form(..., min_length=10, max_length=2000),
):
    # This local demo validates the form and displays a confirmation.
    # Add email/database integration if you need to actually deliver messages.
    return RedirectResponse(url="/?sent=1#contact", status_code=303)
