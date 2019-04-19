import jwt

# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, current_app

# Import password / encryption helper tools
#from werkzeug.security import check_password_hash, generate_password_hash

from werkzeug.datastructures import ImmutableMultiDict

# Import module forms
from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import Group, Role # pylint: disable=unused-import
from app.mod_user.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
MOD_AUTH = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@MOD_AUTH.route('/getkey', methods=['POST'])
def getkey():
    # Get JSON request body
    req = ImmutableMultiDict(request.get_json())

    # If sign in form is submitted
    form = LoginForm(req)

    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            payloads = {"user": user.name, "email": user.email}
            encoded_jwt = jwt.encode(payloads, current_app.config["SECRET_KEY"],
                                     current_app.config["JWT_ALGORITHM"])
            return jsonify({"result": encoded_jwt.decode("utf-8")})
        return jsonify({"result": "Usuário ou senha inválidos!"}), 404
    return jsonify({"result": form.errors}), 406

@MOD_AUTH.route('/decode', methods=['POST'])
def decode():
    # Get APIKey from request head
    key = request.headers.get('Authorization')
    if key:
        try:
            payloads = jwt.decode(key.replace("Bearer ", ""),
                                  current_app.config["SECRET_KEY"],
                                  current_app.config["JWT_ALGORITHM"])
        except jwt.exceptions.DecodeError:
            return jsonify({"result": "Token inválido!"}), 401
        return jsonify({"result": payloads})
    return jsonify({"result": "Token é requerido para esta requisição!"}), 401

@MOD_AUTH.route('/logged', methods=['GET'])
def logged():
    return render_template("auth/logged.html")
