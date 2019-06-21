# Import Form
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from app import DB
import wtforms_json
from app.mod_auth.validator import Unique, Email

wtforms_json.init()

__BaseModelForm = model_form_factory(FlaskForm)

class RestForm(__BaseModelForm):

    # disable csrf
    class Meta:
        #locales = ['pt'] # to force other language
        csrf = False
        email_validator = Email
        unique_validator = Unique

    @classmethod
    def get_session(self):
        return DB.session