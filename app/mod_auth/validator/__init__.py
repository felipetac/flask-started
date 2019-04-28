from wtforms_components import Email
from wtforms_alchemy import Unique

'''
 Customizei estes validadores pois wtforms-alchemy não estava traduzindo
 https://wtforms-alchemy.readthedocs.io/en/latest/validators.html#overriding-default-validators
'''

class EmailValidator(Email):
    def __init__(self, message='Email Inválido.'):
        Email.__init__(self, message=message)

class UniqueValidator(Unique):
    def __init__(self, column, get_session=None, message='Já Existe.'):
        Unique.__init__(self, column, get_session=get_session, message=message)