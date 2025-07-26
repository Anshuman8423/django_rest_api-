# Django REST API (Students)

## Setup
1. Create virtual env and activate:
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate

4. Create admin user:
   python manage.py createsuperuser

5. Run server:
   python manage.py runserver
