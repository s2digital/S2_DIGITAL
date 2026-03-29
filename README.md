# NeonexTech — Simple Flask Website

Minimal Flask app for a company site with pages: Home, About, Products, Services, Contact and a simple chatbot + admin view for contact inquiries.

## Features
- App factory pattern
- Blueprints: `main` (pages + contact) and `chat` (chat API)
- SQLite via Flask-SQLAlchemy
- Simple admin view protected by a query key
- Environment-aware configuration (Dev / Test / Prod)

## Prerequisites
- macOS with Python 3 installed (use `python3`)
- Git (optional)

## Quick setup (project root: /Users/sachinlande/neonextech)
1. Create & activate venv
```bash



cd neonextech
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
cd..
python run.py


# default dev DB: neonextech_dev.db
export DATABASE_URL=sqlite:///neonextech_dev.db
# change admin key (default is "changeme")
export ADMIN_KEY=mysupersecret
# select config (optional)
export NEONEXTECH_CONFIG=neonextech.config.ProdConfig

##
Run tests:
activate your .venv
pip install -r requirements.txt
pytest -q


##
# activate venv
source .venv/bin/activate

# from project root - to have latest added db changes 
source .venv/bin/activate
rm -f neonextech_dev.db neonextech.db
flask --app run.py init-db
python run.py
# run server
python run.py