import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
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
