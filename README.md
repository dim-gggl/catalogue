# Art Archive Tool

This Django project provides a small catalogue application to manage artworks.

## Setup

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and edit the values:

```bash
cp .env.example .env
```

3. Apply migrations and load initial data:

```bash
python src/manage.py migrate
python src/manage.py loaddata src/preloaded_data.json
```

4. Run the development server:

```bash
python src/manage.py runserver
```

5. Run tests:

```bash
python src/manage.py test
```