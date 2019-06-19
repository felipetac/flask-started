from . import RestForm
from app.mod_auth.model.user import User
from wtforms_alchemy import ModelFormField
from .group import GroupForm


class UserForm(RestForm):

    class Meta:
        model = User

    group = ModelFormField(GroupForm)