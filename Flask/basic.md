# FLASK 

Flask is a micro web framework written in Python. It is called “micro” because it provides only core features by default. Uses Werkzeug (WSGI) for request handling and Jinja2 for templating. Highly flexible and extensible with third-party libraries. Commonly used for REST APIs, microservices, and small web apps

### FLASK API

Flask is widely used to build RESTful APIs. Supports HTTP methods: GET, POST, PUT, DELETE, PATCH. APIs usually return JSON responses. Easy integration with authentication, database, and ORMs. Can use extensions like Flask-RESTful, Flask-JWT, and Flask-CORS.

REST API stands for Representational State Transfer Application Programming Interface. It is a way for two systems to communicate over the internet, usually using HTTP. Whereas, FastAPI is a Python web framework used to build REST APIs quickly and efficiently.
👉 REST API = concept / design style
👉 FastAPI = tool/framework to create REST APIs

# Folder Structure

```
project/
│── app/
│   ├── __init__.py
│   ├── routes/
│   │   └── user_routes.py
│   ├── services/
│   │   └── user_service.py
│   ├── models/
│   │   └── user_model.py
│   ├── schemas/
│   │   └── user_schema.py
│   └── config.py
│── templates/
│── static/
│── run.py
│── requirements.txt
```

app/: Core application logic.
routes.py: API endpoints.
models.py: Database models.
templates/: HTML files.
static/: CSS, JS, images.
run.py: Application entry point.

