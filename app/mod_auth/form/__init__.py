# Import Form
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from app import DB
import wtforms_json
from app.mod_auth.validator import EmailValidator, UniqueValidator

wtforms_json.init()

__BMF = model_form_factory(FlaskForm)

class RestForm(__BMF):

    # disable csrf
    class Meta:
        # locales = ['pt'] # to force other language
        csrf = False
        email_validator = EmailValidator
        unique_validator = UniqueValidator

    @classmethod
    def get_session(self):
        return DB.session