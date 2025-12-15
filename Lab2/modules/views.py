from flask import jsonify, request, abort
from modules import app
from modules.models import users, categories, records
import uuid
from datetime import datetime


@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    if not user_data or 'name' not in user_data:
        abort(400, description="Missing 'name' in request body")
    user_id = uuid.uuid4().hex
    user = {"id": user_id, "name": user_data['name']}
    users[user_id] = user
    return jsonify(user)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user)

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"status": "deleted", "id": user_id})
    abort(404, description="User not found")


@app.route('/category', methods=['GET'])
def get_categories():
    return jsonify(list(categories.values()))

@app.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()
    if not data or 'name' not in data:
        abort(400, description="Missing 'name'")
    cat_id = uuid.uuid4().hex
    category = {"id": cat_id, "name": data['name']}
    categories[cat_id] = category
    return jsonify(category)

@app.route('/category/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    if category_id in categories:
        del categories[category_id]
        return jsonify({"status": "deleted", "id": category_id})
    abort(404, description="Category not found")


@app.route('/record', methods=['POST'])
def create_record():
    data = request.get_json()
    if not data or 'user_id' not in data or 'category_id' not in data:
        abort(400, description="Missing user_id or category_id")
    rec_id = uuid.uuid4().hex
    record = {
        "id": rec_id,
        "user_id": data['user_id'],
        "category_id": data['category_id'],
        "amount": data.get('amount', 0),
        "created_at": datetime.now().isoformat()
    }
    records[rec_id] = record
    return jsonify(record)

@app.route('/record/<record_id>', methods=['GET'])
def get_record(record_id):
    record = records.get(record_id)
    if not record:
        abort(404, description="Record not found")
    return jsonify(record)

@app.route('/record/<record_id>', methods=['DELETE'])
def delete_record(record_id):
    if record_id in records:
        del records[record_id]
        return jsonify({"status": "deleted", "id": record_id})
    abort(404, description="Record not found")

@app.route('/record', methods=['GET'])
def get_records_filtered():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')
    if not user_id and not category_id:
        abort(400, description="You must provide user_id or category_id parameters")

    filtered_records = []
    for rec in records.values():
        if user_id and rec['user_id'] != user_id:
            continue
        if category_id and rec['category_id'] != category_id:
            continue
        filtered_records.append(rec)

    return jsonify(filtered_records)