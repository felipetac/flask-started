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

import json

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['POST'])
def signin():

    # get JSON request
    req = ImmutableMultiDict(request.get_json())

    # If sign in form is submitted
    form = LoginForm(req)

    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            return jsonify({"success": True, "result": {"user": user.name, "password": user.password}})
        return jsonify({"success": False, "result": {"flash": ["Usuário ou senha inválidos!"]}})
    return jsonify({"success": False, "result": form.errors})

@mod_auth.route('/logged', methods=['GET'])
def home():
    return render_template("auth/logged.html")