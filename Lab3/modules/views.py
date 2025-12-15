from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from modules import app, db
from modules.models import UserModel, CategoryModel, RecordModel
from modules.schemas import UserSchema, CategorySchema, RecordSchema

@app.route('/user', methods=['POST'])
def create_user():
    schema = UserSchema()
    user_data = schema.load(request.get_json())
    user = UserModel(**user_data)
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        abort(400, message="User with that name already exists.")
    return schema.dump(user)

@app.route('/users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    return jsonify(UserSchema(many=True).dump(users))

@app.route('/category', methods=['POST'])
def create_category():
    schema = CategorySchema()
    data = schema.load(request.get_json())
    category = CategoryModel(**data)
    
    try:
        db.session.add(category)
        db.session.commit()
    except IntegrityError:
        abort(400, message="Category error.")
    return schema.dump(category)

@app.route('/category', methods=['GET'])
def get_categories():
    user_id = request.args.get('user_id')
    
    query = CategoryModel.query.filter(CategoryModel.user_id == None)
    
    if user_id:
        query = CategoryModel.query.filter(
            (CategoryModel.user_id == None) | (CategoryModel.user_id == user_id)
        )
        
    return jsonify(CategorySchema(many=True).dump(query.all()))

@app.route('/record', methods=['POST'])
def create_record():
    schema = RecordSchema()
    data = schema.load(request.get_json())
    record = RecordModel(**data)
    try:
        db.session.add(record)
        db.session.commit()
    except IntegrityError:
        abort(400, message="Invalid user_id or category_id.")
    return schema.dump(record)

@app.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')
    query = RecordModel.query
    if user_id:
        query = query.filter_by(user_id=user_id)
    if category_id:
        query = query.filter_by(category_id=category_id)
    return jsonify(RecordSchema(many=True).dump(query.all()))

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500, message="An error occurred while deleting the user.")
    return jsonify({"message": "User deleted", "id": user_id})