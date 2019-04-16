# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

DB = SQLAlchemy()
MA = Marshmallow()

# Define a base model for other database tables to inherit
class Base(DB.Model):

    __abstract__ = True

    id = DB.Column(DB.Integer, primary_key=True)
    date_created = DB.Column(DB.DateTime, default=DB.func.current_timestamp())
    date_modified = DB.Column(DB.DateTime, default=DB.func.current_timestamp(),
                              onupdate=DB.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name = DB.Column(DB.String(128), nullable=False)

    # Identification Data: email & password
    email = DB.Column(DB.String(128), nullable=False, unique=True)
    password_hash = DB.Column(DB.String(192), nullable=False)

    # Authorisation Data: role & status
    #role = DB.Column(DB.SmallInteger, nullable=False, default=1)

    # INFO: arg 'server_default' neste caso é um FIXED para funcionar o migration no SQLITE
    #role = DB.Column(DB.String(128), nullable=False, default='member')
    #status = DB.Column(DB.String(100), nullable=False, default='active', server_default='active')
    #deleted = DB.Column(DB.String(3), nullable=False,
    #                    default='no', server_default='no') #coluna de test migration

    # New instance instantiation procedure
    #def __init__(self, name, email, password):
    #    self.name = name
    #    self.email = email
    #    self.password = password

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def hydrate(self, form):
        """
        Hydrate form data into user model
        """
        self.name = form.name.data
        self.email = form.email.data
        self.password = form.password.data

    def __repr__(self):
        return '<User %r>' % (self.name)

class UserSchema(MA.ModelSchema):
    class Meta:
        model = User
