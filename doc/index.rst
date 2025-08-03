==============================
Django Project Documentation
==============================

Project Description
===================

This project is a modular Django web application for managing user profiles and rental listings ("lettings").  
It was designed with scalability in mind and includes testing, CI/CD integration, error monitoring, and production deployment.

Project Installation
====================

Requirements:

- Python 3.12
- Git
- Docker + Docker Compose (optional for local use)
- Internet access to install dependencies
- A `.env` file with required environment variables

Steps:

1. Clone the repository:
git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Start the local server:
python manage.py runserver


Quick Start Guide
=================

If Docker is installed, you can run the application with:

.. code-block:: bash

   docker build -t oc-lettings-site .
   docker run -p 8000:8000 --env-file .env oc-lettings-site

The application will be available at: http://localhost:8000

Technologies and Languages Used
===============================

- Python 3.12
- Django 3.0
- Gunicorn (for production)
- Docker
- GitHub Actions (CI/CD)
- Render (hosting platform)
- Sentry (error monitoring)
- SQLite3 (default database)

Database Models
===============

**Letting**

- `title`: CharField
- `address`: ForeignKey to `Address`

**Address**

- `number`, `street`, `city`, `state`, `zip_code`, `country_iso_code`

**Profile**

- `user`: OneToOneField to `User`
- `favorite_city`: CharField

**User (auth.User)**  
- Built-in Django user model

Programming Interfaces (APIs)
=============================

This project does not include a REST API. All views are standard HTML rendered views:

- `/lettings/`: List of lettings
- `/lettings/<id>/`: Letting detail
- `/profiles/`: List of user profiles
- `/profiles/<username>/`: Profile detail

Each route is handled by a function-based view in `views.py`, with associated HTML templates.

User Guide
==========

Use cases:

1. **Display all user profiles**: `/profiles/`
2. **View details of a specific profile**: `/profiles/<username>/`
3. **List available lettings**: `/lettings/`
4. **Show detail of a specific letting**: `/lettings/<id>/`

Admin panel: available at `/admin/` after creating a superuser:

.. code-block:: bash

   python manage.py createsuperuser

Deployment
==========

CI/CD is automated via GitHub Actions:

- `master` branch:
- Linting + Tests + coverage > 80%
- Build Docker image
- Push image to Docker Hub
- Manual deployment via Render

Environment variables must be configured in `.env` or in Render settings:

.. code-block:: text

   DEBUG=False
   SECRET_KEY=changeme
   ALLOWED_HOSTS=my-app.onrender.com
   SENTRY_DSN=<optional>

Static files collection:

.. code-block:: bash
   
   python manage.py collectstatic --noinput

Database: uses SQLite3 by default. No remote configuration needed.

To deploy production updates:

1. Push code to `master`
2. Wait for Docker Hub image build
3. Trigger manual deploy on Render ("Manual Deploy")

Application Management
======================

- **Tests**: `pytest --cov=.` (expected coverage: >80%)
- **Linting**: `flake8 .`
- **Logs & errors**: sent to Sentry (if configured)
- **Static files**: served via `whitenoise` in production
