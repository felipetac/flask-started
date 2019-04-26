# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField  # BooleanField

# Import Form validators
from wtforms.validators import Required, Email

from app.mod_auth.form import RestForm
from app.mod_auth.model.role import Role


class RoleForm(RestForm):

    class Meta:
        model = Role
