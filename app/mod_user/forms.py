# Import Form
from flask_wtf import FlaskForm  

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo

class RestForm(FlaskForm):
    
    # disable csrf
    class Meta:
        csrf = False

# Define the login form (WTForms)
class LoginForm(RestForm):
    
    email = TextField('Email Address', [Email(),
                      Required(message='E-mail é requerido! preenche-o.')])
    password = PasswordField('Password', [
                             Required(message='Precisa fornecer uma senha.')])

class UserForm(RestForm):

    name = TextField('Username', [
                             Required(message='Precisa fornecer o nome do usuário.')])
    email = TextField('Email Address', [Email(),
                      Required(message='E-mail é requerido! preenche-o.')])
    password = PasswordField('Password', [
                             Required(message='Precisa fornecer uma senha.')])