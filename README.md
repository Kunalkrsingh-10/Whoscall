# Whoscall

Whoscall is a Django-based and django rest framework based project designed to manage and identify contacts, including spam detection features. This README provides an overview of the project, how to set it up, and how to contribute.

### Prerequisites

- Python 3.x
- Django
- SQLite (default database)


# Usage 
- The application allows you to manage contacts and identify spam callers.
- You can interact with the API endpoints to create, read, update, and delete contacts.
- Use tools like Postman or CURL to test the API endpoints.

Whoscall/
│
- ├── Api/
- │   ├── migrations/
- │   ├── __init__.py
- │   ├── admin.py
- │   ├── apps.py
- │   ├── models.py
- │   ├── serializers.py
- │   ├── tests.py
- │   ├── urls.py
- │   └── views.py
- │
- ├── Whoscall/
- │   ├── __init__.py
- │   ├── asgi.py
- │   ├── settings.py
- │   ├── urls.py
- │   └── wsgi.py
- │
- ├── manage.py
- └── db.sqlite3
1. **Clone the repository:**

   ```sh
   git clone https://github.com/username/whoscall.git
   cd whoscall/Whoscall

