# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField, IntegerField  # BooleanField

# Import Form validators
from wtforms.validators import Required, Email

from app.mod_auth.form import RestForm
from app.mod_auth.model.user import User


class UserForm(RestForm):

    class Meta:
        model = User
        group_id = IntegerField("Id do Grupo")