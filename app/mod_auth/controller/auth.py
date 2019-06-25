import jwt

# Import flask dependencies
from flask import request, render_template, jsonify, current_app

# Import password / encryption helper tools
#from werkzeug.security import check_password_hash, generate_password_hash

#from werkzeug.datastructures import ImmutableMultiDict

from app.mod_auth.model.user import User
from app.mod_auth.controller import MOD_AUTH

# Import module forms
from app.mod_auth.form.auth import LoginForm

# Set the route and accepted methods
@MOD_AUTH.route('/getkey', methods=['POST'])
def getkey():

    # Get JSON request body
    #req = ImmutableMultiDict(request.get_json())

    # If sign in form is submitted
    #form = LoginForm(req)

    form = LoginForm.from_json(request.get_json())

    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
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
