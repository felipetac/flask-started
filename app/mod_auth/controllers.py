# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

from werkzeug.datastructures import ImmutableMultiDict

# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import User

# For import app config's 
from flask import current_app as app

import json
import jwt

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/getkey', methods=['POST'])
def getkey():

    # Get JSON request body
    req = ImmutableMultiDict(request.get_json())

    # If sign in form is submitted
    form = LoginForm(req)

    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            payloads = {"user": user.name, "email": user.email, 
                        "role": user.role, "status": user.status}
            encoded_jwt = jwt.encode(payloads, app.config["SECRET_KEY"], app.config["JWT_ALGORITHM"])
            return jsonify({"result": encoded_jwt.decode("utf-8")})
        return jsonify({"result": "Usuário ou senha inválidos!"}), 404
    return jsonify({"result": form.errors}), 406

@mod_auth.route('/decode', methods=['POST'])
def decode():
    # Get APIKey from request head 
    key = request.headers.get('Authorization')
    
    if key:
        try:
            payloads = jwt.decode(key.replace("Bearer ", ""), app.config["SECRET_KEY"], app.config["JWT_ALGORITHM"])
        except jwt.exceptions.DecodeError:
            return jsonify({"result": "Token inválido!"}), 401
        return jsonify({"result": payloads})
    return jsonify({"result": "Token é requerido para esta requisição!"}), 401
    

@mod_auth.route('/logged', methods=['GET'])
def logged():
    return render_template("auth/logged.html")