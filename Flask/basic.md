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
services/: business logic from API routes

# ORM (Object Relational Mapping)

ORM is a technique that maps database tables to Python classes. Allows developers to interact with the database using objects instead of SQL queries. Improves code readability, maintainability, and productivity.  
Each class → table  
object → row  
attribute → column  

## ORM in Flask

Commonly used ORM is SQLAlchemy. Flask integrates ORM using Flask-SQLAlchemy. Handles CRUD operations, relationships, and migrations. Provides database abstraction, making apps database-agnostic. Supports relationships (one-to-one, one-to-many, many-to-many)

### SQLAlchemy.relationship()

relationship() is used to define relationships between ORM models. It connects Python objects, not database columns directly. Used along with ForeignKey to establish table relationships. Supports lazy loading and bidirectional access.

#### Key Parameters  
**back_populates / backref:** Enables two-way relationship.  
**lazy:** Controls how related data is loaded (select, joined, subquery). Controls how related objects are loaded:
select (default): Load on access (lazy loading).  
joined: Load using JOIN (eager loading).  
subquery: Load with subquery (eager loading).  
dynamic: Returns a query object instead of a list.  
**cascade:** Defines behavior on delete/update (all, delete-orphan). Common options:  
'all' → all operations cascade  
'delete' → delete related objects  
'delete-orphan' → delete child if unlinked  
**uselist:** Used for one-to-one relationships.

```
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    profile = db.relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete"
    )

    posts = db.relationship(
        "Post",
        back_populates="user",
        cascade="all, delete",
        lazy = "select"
    )
```

While developing API, the specification of the API or diff way of passing the parameter
path variable(http://127.0.0.1:5000/users/users_by_ids/4)
query parameter(http://127.0.0.1:5000/users/users_by_ids?id=2&id=3&name=Parvathi)

# native query

# headers

# exception
