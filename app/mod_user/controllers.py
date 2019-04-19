from flask import Blueprint, request, jsonify
from werkzeug.datastructures import ImmutableMultiDict
from app.container import DB
from app.mod_user.forms import UserForm
from app.mod_user.models import User, UserSchema

# Define the blueprint: 'auth', set its url prefix: app.url/auth
MOD_USER = Blueprint('user', __name__, url_prefix='/user')

@MOD_USER.route('', methods=['GET'])
def list_users():
    users = User.query.all()
    if users:
        user_schema = UserSchema(many=True)
        return jsonify(user_schema.dump(users).data)
    return jsonify("Não há usuários cadastrados na base!"), 204

@MOD_USER.route('/<int:id>', methods=['GET'])
def read_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user).data)
    return jsonify("Não há usuários cadastrados na base!"), 204

@MOD_USER.route('', methods=['POST'])
def create_user():
    req = ImmutableMultiDict(request.get_json())
    form = UserForm(req)
    if form.validate_on_submit():
        user = User()
        user.hydrate(form)
        DB.session.add(user)
        DB.session.commit()
        return jsonify("Usuário criado com sucesso!")
    return jsonify(form.errors), 406

@MOD_USER.route('/<int:id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        req = ImmutableMultiDict(request.get_json())
        form = UserForm(req)
        if form.validate_on_submit():
            user.hydrate(form)
            DB.session.commit()
            return jsonify("Usuário atualizado com sucesso!")
        return jsonify(form.errors), 406
    return jsonify("Id de usuário não encontrado!"), 204

@MOD_USER.route('/<int:id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        DB.session.delete(user)
        DB.session.commit()
        return jsonify("Usuário apagado com sucesso!")
    return jsonify("Id de usuário não encontrado ou já deletado!"), 204
