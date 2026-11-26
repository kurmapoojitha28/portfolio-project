# Personal Portfolio — FastAPI

A server-side rendered portfolio using FastAPI, Jinja2 templates, static files, and cookie-based Light/Dark theme preference.

## Requirements
- Python 3.10+
- pip

## Run locally (Windows PowerShell)
```powershell
cd portfolio_app
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000 in your browser.

If PowerShell blocks virtual environment activation, use:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Customize
- Replace “Your Name” and the biography in `templates/index.html`.
- Put your own headshot at `static/images/profile.jpg`.
- Edit skills and project dictionaries in `main.py`.
- Update project URLs to your actual repositories.

## Features
- Jinja2 base template inheritance and dynamic project iteration
- Static assets resolved using `url_for`
- Theme toggle persisted in a 30-day HttpOnly, SameSite=Lax cookie
- Contact form validation and 303 redirect confirmation (demo; no email is sent)
- Project filtering using `/?tech=Python`

## Theme cookie verification
Toggle the theme, then open browser DevTools → Application (or Storage) → Cookies → `http://127.0.0.1:8000`. The `theme` cookie should have HttpOnly enabled and a Max-Age of 2592000 seconds.
