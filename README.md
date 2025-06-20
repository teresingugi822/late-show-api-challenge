# Late Show API Challenge

A RESTful API built with **Flask** for a Late Night TV show.  
Supports **PostgreSQL**, **JWT Authentication**, and a clean **MVC** structure.

---

## 🚀 Setup Instructions
1. Install dependencies:
    ```bash
    pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
    ```
2. Create the database:
    ```sql
    CREATE DATABASE late_show_db;
    ```
3. Set environment variables in `.env`:
    ```
    DATABASE_URL=postgresql://user:pass@localhost:5432/late_show_db
    JWT_SECRET_KEY=yoursecretkey
    ```
4. Initialize database:
    ```bash
    export FLASK_APP=server/app.py
    flask db init
    flask db migrate -m "initial migration"
    flask db upgrade
    python server/seed.py
    ```

---

## 🗺️ Routes
| Route                           | Method | Auth? | Description                           |
|-----------------------------|--------|------|-----------------------------|
| /register                 | POST    | ❌    | Register new user          |
| /login                    | POST    | ❌    | Get JWT access token       |
| /episodes                | GET     | ❌    | List all episodes            |
| /episodes/<id>           | GET     | ❌    | Get episode + appearances  |
| /episodes/<id>           | DELETE  | ✅    | Delete an episode           |
| /guests                   | GET     | ❌    | List all guests            |
| /appearances             | POST    | ✅    | Create new appearance       |

---

## 🔐 Auth Flow
1. **Register** user
2. **Login** and obtain an **access token**
3. In protected requests, send:
    ```
    Authorization: Bearer <token>
    ```

---

## ⚡️ Sample Request & Response
**POST /register**
```json
{
  "username": "john",
  "password": "pass123"
}
