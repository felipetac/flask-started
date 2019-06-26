from app import DB
from app.mod_auth.model.user import User as UserModel, UserSchema
from app.mod_auth.service.group import Group as GroupService
from app.mod_auth.form.user import UserForm

class User():

    @staticmethod
    def list():
        users = UserModel.query.all()
        if users:
            user_schema = UserSchema(many=True)
            return user_schema.dump(users)
        return []

    @staticmethod
    def read(user_id, serializer=True):
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            if serializer:
                user_schema = UserSchema()
                return user_schema.dump(user)
            return user
        return None

    @classmethod
    def edit(cls, json_obj):
        user, flag = UserModel(), False
        if "id" in json_obj.keys():
            user = cls.read(json_obj["id"], serializer=False)
            flag = True
        if user:
            form = UserForm.from_json(json_obj, obj=user) # set the object to avoid raising a ValidationError
            form.group_id.choices = GroupService.get_choices()
            if form.validate_on_submit():
                form.populate_obj(user)
                if not flag:
                    DB.session.add(user)
                DB.session.commit()
                user_schema = UserSchema()
                return user_schema.dump(user) # Return user with last id insert
            return {"errors": form.errors}
        return None

    @classmethod
    def delete(cls, user_id):
        user = cls.read(user_id, serializer=False)
        if user:
            DB.session.delete(user)
            DB.session.commit()
            return True
        return None