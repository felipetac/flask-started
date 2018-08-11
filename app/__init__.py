import os

# Import flask and template operators
from flask import Flask, render_template, jsonify

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

from config import config

# Define the WSGI application object
app = Flask(__name__)

# Configurations
#app.config.from_object('config')
app.config.from_object(config.get(os.environ["APP_SETTINGS"] or "default"))

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Object serialization and deserialization, lightweight and fluffy
ma = Marshmallow(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"result": "Url não encontrada..."}), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_user.controllers import mod_user as user_module
from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(user_module)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()