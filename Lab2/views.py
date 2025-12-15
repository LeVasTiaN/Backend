from Lab2 import app
from Lab2.models import users, categories, records
from flask import request, jsonify
import uuid
from datetime import datetime

@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user_id = uuid.uuid4().hex
    user = {"id": user_id, "name": user_data.get("name")}
    users[user_id] = user 
    return jsonify(user)