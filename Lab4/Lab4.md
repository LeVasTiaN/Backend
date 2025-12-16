# Lab 4: Authentication & JWT

**Variant:** 32 ≈ 2 (Custom Categories)

## Project Structure
* `modules/`: Application source code (`models.py`, `views.py`, `schemas.py`, `config.py`).
* `migrations/`: Database migration scripts for password storage.
* `Dockerfile`: Container configuration with auto-migration command.
* `docker-compose.yaml`: Local development stack (App + PostgreSQL).

## Prerequisites
* Python 3.11+
* Docker & Docker Compose
* Postman (for testing API endpoints)

---

## How to Run

1.  **Open the directory:**
    ```bash
    cd Lab4
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