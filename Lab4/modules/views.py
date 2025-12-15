from flask import jsonify, request
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from modules import app, db
from modules.models import UserModel, CategoryModel, RecordModel
from modules.schemas import UserSchema, CategorySchema, RecordSchema


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        abort(400, message="Missing username or password")
    if UserModel.query.filter_by(username=data["username"]).first():
        abort(400, message="Username already exists")
    hashed_password = pbkdf2_sha256.hash(data["password"])
    user = UserModel(username=data["username"], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = UserModel.query.filter_by(username=data.get("username")).first()

    if user and pbkdf2_sha256.verify(data.get("password"), user.password):
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token)

    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/category', methods=['GET'])
@jwt_required()
def get_categories():
    current_user_id = get_jwt_identity()
    query = CategoryModel.query.filter(
        (CategoryModel.user_id == None) | (CategoryModel.user_id == current_user_id)
    )
    return jsonify(CategorySchema(many=True).dump(query.all()))

@app.route('/category', methods=['POST'])
@jwt_required()
def create_category():
    current_user_id = get_jwt_identity()
    schema = CategorySchema()
    data = schema.load(request.get_json())
    user_id_to_save = current_user_id
    if "user_id" in data and data["user_id"] is None:
        user_id_to_save = None
    category = CategoryModel(name=data["name"], user_id=user_id_to_save)
    try:
        db.session.add(category)
        db.session.commit()
    except IntegrityError:
        abort(400, message="Category error.")
    return schema.dump(category)

@app.route('/record', methods=['POST'])
@jwt_required()
def create_record():
    current_user_id = get_jwt_identity()
    schema = RecordSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400
    record = RecordModel(
        user_id=current_user_id,
        category_id=data["category_id"],
        amount=data["amount"]
    )
    try:
        db.session.add(record)
        db.session.commit()
        db.session.refresh(record)
    except IntegrityError:
        db.session.rollback()
        abort(400, message="Invalid category_id.")
    return schema.dump(record), 201

@app.route('/record', methods=['GET'])
@jwt_required()
def get_records():
    current_user_id = get_jwt_identity()
    category_id = request.args.get('category_id')
    query = RecordModel.query.filter_by(user_id=current_user_id)
    if category_id:
        query = query.filter_by(category_id=category_id)
    return jsonify(RecordSchema(many=True).dump(query.all()))

@app.route('/user/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    current_user_id = get_jwt_identity()
    if str(user_id) != str(current_user_id):
        abort(403, message="You can only delete your own account.")
    user = UserModel.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted", "id": user_id})