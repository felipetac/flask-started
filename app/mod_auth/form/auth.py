# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email

from app.mod_auth.form import RestForm

# Define the login form (WTForms)
class LoginForm(RestForm):
    email = TextField('Email Address',
                      [Email(),
                       Required(message='E-mail é requerido! preenche-o.')])
    password = PasswordField('Password',
                             [Required(message='Precisa fornecer uma senha.')])
