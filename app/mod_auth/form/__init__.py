# Import Form
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from app import DB
import wtforms_json

wtforms_json.init()

__BMF = model_form_factory(FlaskForm)

class RestForm(__BMF):

    # disable csrf
    class Meta:
        # locales = ['pt'] # to force other language
        csrf = False

    @classmethod
    def get_session(self):
        return DB.session