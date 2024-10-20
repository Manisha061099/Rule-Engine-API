# Rule-Engine-API
**Technologies Used**
Flask: Web framework for building the API.
SQLAlchemy: ORM for database interactions (if used).
PostgreSQL/MySQL/SQLite: Choice of relational database (or any other of your choice).
**Setup Instructions
Prerequisites**
Python 3.x
Flask
A database (PostgreSQL, MySQL, SQLite, etc.)

**Install Dependencies:**

pip install Flask SQLAlchemy
**Run the Application:**
python app.py

**Create Rule Through POSTMAN**
POST /create_rule
{
    "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))"
}
**Combine Rules** 
POST /combine_rules
{
    "rules": [
        "((age > 30 AND department = 'Sales'))",
        "((age < 25 AND department = 'Marketing'))"
    ]
}
