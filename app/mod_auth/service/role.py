from app import DB
from app.mod_auth.model.role import Role as RoleModel, RoleSchema
from app.mod_auth.form.role import RoleForm

class Role():

    @staticmethod
    def list():
        roles = RoleModel.query.all()
        if roles:
            role_schema = RoleSchema(many=True)
            return role_schema.dump(roles)
        return []

    @staticmethod
    def read(role_id, serialize=True):
        role = RoleModel.query.filter_by(id=role_id).first()
        if role:
            role_schema = RoleSchema()
            if serialize:
                return role_schema.dump(role)
            return role
        return None

    @classmethod
    def edit(cls, json_obj):
        role, flag = RoleModel(), False
        if "id" in json_obj.keys():
            role = cls.read(json_obj["id"], serialize=False)
            flag = True
        if role:
            form = RoleForm.from_json(json_obj, obj=role) # set the object to avoid raising a ValidationError
            if form.validate_on_submit():
                form.populate_obj(role)
                if not flag:
                    DB.session.add(role)
                DB.session.commit()
                role_schema = RoleSchema()
                return role_schema.dump(role) # Return role with last id insert
            return {"errors": form.errors}
        return None

    @classmethod
    def delete(cls, role_id):
        role = cls.read(role_id, serialize=False)
        if role:
            DB.session.delete(role)
            DB.session.commit()
            return True
        return None

    @staticmethod
    def get_choices():
        choices = RoleModel.query.with_entities(RoleModel.id, RoleModel.name)
        if choices:
            role_schema = RoleSchema(many=True, only=('id', 'name'))
            return [(r["id"], r["name"]) for r in role_schema.dump(choices)]
        return []