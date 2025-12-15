from modules.db import db
from sqlalchemy.sql import func

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    records = db.relationship("RecordModel", back_populates="user", lazy="dynamic", cascade="all, delete")
    categories = db.relationship("CategoryModel", back_populates="user", lazy="dynamic", cascade="all, delete")

class CategoryModel(db.Model):
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    user = db.relationship("UserModel", back_populates="categories")
    records = db.relationship("RecordModel", back_populates="category", lazy="dynamic")

class RecordModel(db.Model):
    __tablename__ = "records"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    amount = db.Column(db.Float(precision=2), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    user = db.relationship("UserModel", back_populates="records")
    category = db.relationship("CategoryModel", back_populates="records")