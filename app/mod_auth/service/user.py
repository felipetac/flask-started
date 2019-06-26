from app import DB
from app.mod_auth.model.user import User as UserModel, UserSchema
from app.mod_auth.model.group import Group
from app.mod_auth.form.user import UserForm

class User():

    def list(self):
        users = UserModel.query.all()
        if users:
            user_schema = UserSchema(many=True)
            return {"success": True, "result": user_schema.dump(users)}
        return {"success": False, "result": []}

    def create(self, json_obj):
        form = UserForm.from_json(json_obj)
        form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            DB.session.add(user)
            DB.session.commit()
            user_schema = UserSchema()
            return {"success": True, "result": user_schema.dump(user)} # Return user with last id insert
        return {"success": False, "result": form.errors}

    def read(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            user_schema = UserSchema()
            return {"success": True, "result": user_schema.dump(user)}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}

    def edit(self, json_obj):
        user, flag = UserModel(), False
        if "id" in json_obj.keys():
            user = UserModel.query.filter_by(id=json_obj["id"]).first()
            flag = True
        if user:
            form = UserForm.from_json(request.get_json(), obj=user) # set the object to avoid raising a ValidationError
            form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]
            if form.validate_on_submit():
                form.populate_obj(user)
                if not flag:
                    DB.session.add(user)
                DB.session.commit()
                user_schema = UserSchema()
                return {"success": True, "result": user_schema.dump(user)} # Return user with last id insert
            return {"success": False, "result": form.errors}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}

    def delete(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            DB.session.delete(user)
            DB.session.commit()
            return {"success": True, "result": "Usuário apagado com sucesso!"}
        return {"success": False, "result": {"id": "Identificador não encontrado!"}}