# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField  # BooleanField

# Import Form validators
from wtforms.validators import Required, Email

from app.mod_auth.form import RestForm
from app.mod_auth.form.user import UserForm
from app.mod_auth.form.role import RoleForm
from app.mod_auth.model.group import Group

from wtforms import IntegerField
from wtforms_alchemy import ModelForm, ModelFieldList, ModelFormField
from wtforms.fields import FormField

class GroupForm(RestForm):

    class Meta:
        model = Group
        parent_id = IntegerField("Id do Grupo Pai")
        users = ModelFieldList(FormField(UserForm))
        roles = ModelFieldList(FormField(RoleForm))
