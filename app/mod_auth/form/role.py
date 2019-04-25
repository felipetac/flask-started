# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField  # BooleanField

# Import Form validators
from wtforms.validators import Required, Email

from app.mod_auth.form import RestForm


class RoleForm(RestForm):

    name = TextField('Nome da Regra',
                     [Required(message='Precisa fornecer o nome da regra.')])
    description = TextField('Descrição da Regra',
                            [Required(message='Precisa fornecer a descrição da regra')])
