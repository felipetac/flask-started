from app.mod_auth.model.user import User
from functools import wraps
from flask import request, jsonify, current_app
import jwt

class Auth():
    def required(role_name=None):
        def decorator(f):
            @wraps(f)
            def wrap(*args, **kwargs):
                key = request.headers.get('Authorization')
                if key:
                    try:
                        payloads = jwt.decode(key.replace("Bearer ", ""),
                                              current_app.config["SECRET_KEY"],
                                              current_app.config["JWT_ALGORITHM"])
                    except jwt.exceptions.DecodeError:
                        return jsonify({"result": "Token inválido!"}), 401
                    user = User.query.filter_by(email=payloads["email"]).first()
                    if user:
                        if role_name in [role.name for role in user.group.roles]:
                            return f(*args, **kwargs)
                        return  jsonify({"result": "Token não possui autorização para efetuar esta requisição!"}), 401
                    return jsonify({"result": "Token inválido!"}), 401
                else:
                    return jsonify({"result": "Token é requerido para esta requisição!"}), 401
            return wrap
        return decorator