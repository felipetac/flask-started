from flask import jsonify
from app.container import APP, DB
from app.mod_auth.controllers import MOD_AUTH
from app.mod_user.controllers import MOD_USER

# Sample HTTP error handling
@APP.errorhandler(404)
def not_found(error): # pylint: disable=unused-argument
    return jsonify({"result": "Url não encontrada..."}), 404

# Register blueprint(s)
APP.register_blueprint(MOD_AUTH)
APP.register_blueprint(MOD_USER)

# Build the database:
# This will create the database file using SQLAlchemy
DB.create_all()
