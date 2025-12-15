from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from modules.db import db
from modules.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

import modules.views