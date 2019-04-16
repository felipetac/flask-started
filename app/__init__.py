import os
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import CONFIG

# Import a modules
from app.mod_user.controllers import MOD_USER
from app.mod_auth.controllers import MOD_AUTH

# Define the WSGI application object
APP = Flask(__name__)

# Configurations
__ENV = os.environ["APP_SETTINGS"] if "APP_SETTINGS" in os.environ.keys() else "default"
APP.config.from_object(CONFIG.get(__ENV))

# Define the database object which is imported
# by modules and controllers
DB = SQLAlchemy(APP)

# Object serialization and deserialization, lightweight and fluffy
MA = Marshmallow(APP)

# Sample HTTP error handling
@APP.errorhandler(404)
def not_found(error): # pylint: disable=unused-argument
    return jsonify({"result": "Url não encontrada..."}), 404

# Register blueprint(s)
APP.register_blueprint(MOD_USER)
APP.register_blueprint(MOD_AUTH)

# Build the database:
# This will create the database file using SQLAlchemy
DB.create_all()
