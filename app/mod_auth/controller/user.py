from flask import request, jsonify
from app import DB
from app.mod_auth.model.group import Group
from app.mod_auth.model.user import User, UserSchema
from app.mod_auth.form.user import UserForm
from app.mod_auth.controller import MOD_AUTH


@MOD_AUTH.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    if users:
        user_schema = UserSchema(many=True)
        return jsonify(user_schema.dump(users))
    return jsonify("Não há usuários cadastrados na base!"), 204


@MOD_AUTH.route('/user', methods=['POST'])
def create_user():
    form = UserForm.from_json(request.get_json())
    form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        DB.session.add(user)
        DB.session.commit()
        return jsonify("Usuário criado com sucesso!")
    return jsonify(form.errors), 406


@MOD_AUTH.route('/user/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user))
    return jsonify("Não há usuários cadastrados na base!"), 204


@MOD_AUTH.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        form = UserForm.from_json(request.get_json(), obj=user) # set the object to avoid raising a ValidationError  
        form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]
        if form.validate_on_submit():
            form.populate_obj(user)
            DB.session.commit()
            return jsonify("Usuário atualizado com sucesso!")
        return jsonify(form.errors), 406
    return jsonify("Id de usuário não encontrado!"), 204


@MOD_AUTH.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        DB.session.delete(user)
        DB.session.commit()
        return jsonify("Usuário apagado com sucesso!")
    return jsonify("Id de usuário não encontrado ou já deletado!"), 204
