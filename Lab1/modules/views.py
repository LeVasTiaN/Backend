from modules import app
from flask import jsonify
import datetime

@app.route('/healthcheck')
def healthcheck():
    return jsonify({
        "status": "OK",
        "date": datetime.datetime.now().isoformat()
    }), 200