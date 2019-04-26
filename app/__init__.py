import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_babel import Babel
from config import CONFIG

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

# Babel adds i18n and l10n support to any Flask application 
BA = Babel(APP)

# Sample HTTP error handling
@APP.errorhandler(404)
def not_found(error):
    ret = error.args if error.args else "Url não encontrada..."
    return jsonify({"result": ret}), 404

# Register blueprint(s)
from app.mod_auth.controller import * # pylint: disable=wrong-import-position
APP.register_blueprint(MOD_AUTH)

# Build the database:
# This will create the database file using SQLAlchemy
DB.create_all()
