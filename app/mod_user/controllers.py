# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

# Import password / encryption helper tools
from werkzeug.security import check_password_hash, generate_password_hash

from werkzeug.datastructures import ImmutableMultiDict

# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_user.forms import UserForm

# Import module models (i.e. User)
from app.mod_user.models import User, UserSchema

# For import app config's 
from flask import current_app as app

import json
import jwt

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_user = Blueprint('user', __name__, url_prefix='/user')

@mod_user.route('', methods=['GET'])
def list_users():
    users = User.query.all()  
    if users:
        user_schema = UserSchema(many=True)
        return jsonify(user_schema.dump(users).data)
    return jsonify("Não há usuários cadastrados na base!"), 404

@mod_user.route('/<int:id>', methods=['GET'])
def read_user(id):
    user = User.query.filter_by(id=id).first()
    if user:
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user).data)
    return jsonify("Não há usuários cadastrados na base!"), 404

@mod_user.route('', methods=['POST'])
def create_user():
    req = ImmutableMultiDict(request.get_json())
    form = UserForm(req)
    if form.validate_on_submit():
        user = User()
        user.hydrate(form)
        db.session.add(user)
        db.session.commit()
        return jsonify("Usuário criado com sucesso!")
    return jsonify(form.errors), 406

@mod_user.route('/<int:id>', methods=['PUT'])
def update_user(id):    
    user = User.query.filter_by(id=id).first()
    if user:
        req = ImmutableMultiDict(request.get_json())
        form = UserForm(req)
        if form.validate_on_submit():     
            user.hydrate(form)
            db.session.commit()
            return jsonify("Usuário atualizado com sucesso!")
        return jsonify(form.errors), 406
    return jsonify("Id de usuário não encontrado!"), 404

@mod_user.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify("Usuário apagado com sucesso!")
    return jsonify("Id de usuário não encontrado ou já deletado!"), 404