## Lab 2: Expense Tracker REST API

## Project Structure
* `modules/`: Contains the application source code (`views.py`, `models.py`).
* `Dockerfile`: Configuration for containerizing the application.
* `docker-compose.yaml`: Configuration for running the app locally with Docker.

## Prerequisites
* Python 3.11+
* Docker & Docker Compose
* Postman (for testing)

---

## How to Run

1. **Open the directory:**

    ```cd Lab2```

3.  **Build and Start:**
    ```bash
    docker-compose up --build
    ```
4.  **Access the API:**
    * Base URL: `http://127.0.0.1:5000`
    * Test Endpoint: `http://127.0.0.1:5000/users`
