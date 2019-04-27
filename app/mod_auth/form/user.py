from . import RestForm
from app.mod_auth.model.user import User
from wtforms import IntegerField
from .group import GroupForm


class UserForm(RestForm):

    class Meta:
        model = User

    group_id = IntegerField("Id do Grupo")