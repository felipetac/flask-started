# Import Form
from flask_wtf import FlaskForm  

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo

# Define the login form (WTForms)
class LoginForm(FlaskForm):
    # disable csrf
    class Meta:
        csrf = False

    email = TextField('Email Address', [Email(),
                      Required(message='E-mail é requerido! preenche-o.')])
    password = PasswordField('Password', [
                             Required(message='Precisa fornecer uma senha.')])