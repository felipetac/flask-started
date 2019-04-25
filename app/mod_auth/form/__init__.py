# Import Form
from flask_wtf import FlaskForm

class RestForm(FlaskForm):

    # disable csrf
    class Meta:
        csrf = False