# Lab 3: Expense Tracker with Database & ORM

**Variant:** 32 ≈ 2 (Custom Categories)

## Project Structure
* `modules/`: Application code (`models.py`, `schemas.py`, `views.py`, etc.).
* `migrations/`: Database migration versions.
* `Dockerfile`: Container configuration with auto-migration command.
* `docker-compose.yaml`: Local development stack (App + PostgreSQL).

## Prerequisites
* Python 3.11+
* Docker & Docker Compose
* Postman (with Lab 3 Collection)

---

## How to Run

1.  **Open the directory:**
    ```bash
    cd Lab3
    ```

2.  **Build and Start:**
    ```bash
    docker-compose up -d --build
    ```

3.  **Initialize Database:**
    ```bash
    docker-compose exec modules flask db upgrade
    ```

4.  **Access the API:**
    * **Base URL:** `http://127.0.0.1:5000`
    * **Test Variant 2 (Using Postman):**
        * **Create Public Category:**
            * Method: `POST` to `/category`
            * Body: `{"name": "General", "user_id": null}`
        
        * **Create Private Category:**
            * Method: `POST` to `/category`
            * Body: `{"name": "Private", "user_id": 1}`