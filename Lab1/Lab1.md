## Lab 1: Project Setup & Basic REST API


### 1. Setup & Running Locally (No Docker)

First, open the lab directory:
```cd Lab1```

Create and activate a virtual environment:

## Linux/macOS
```python3 -m venv env```

```source env/bin/activate```

## Windows
```python -m venv env```

```.\env\Scripts\activate```

### Install dependencies
```pip install -r requirements.txt```

### Run the application 
```flask --app modules run --host 0.0.0.0 -p 8080```

### Open the browser:
http://localhost:8080/healthcheck

## 2. Running with Docker Compose

Just run
```docker-compose up --build```

And the application will be accesible at http://localhost:8080/healthcheck

To stop the application, enter 
```docker-compose down```