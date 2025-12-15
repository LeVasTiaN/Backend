import os

class Config:
    API_TITLE = "Finance REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret-key")