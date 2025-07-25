# FastAPI To-Do App

This is a simple CRUD API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

## Features
- Create, Read, Update, and Delete to-do items
- PostgreSQL for persistent storage
- Auto-generated docs at `/docs`

## Setup Instructions

1. Clone the repo
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file:
    ```
    DATABASE_URL=postgresql://postgres:postgres@localhost:5432/todolistdb
    ```

4. Run the server:
    ```bash
    uvicorn main:app --reload
    ```

## License
MIT
