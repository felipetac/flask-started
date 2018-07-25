# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    __tablename__ = 'auth_user'

    # User Name
    name = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorisation Data: role & status
    #role = db.Column(db.SmallInteger, nullable=False, default=1)
    # INFO: arg 'server_default' neste caso é um FIXED para funcionar o migration no SQLITE
    role = db.Column(db.String(128), nullable=False, default='member')
    status = db.Column(db.String(100), nullable=False, default='active', server_default='active')
    deleted = db.Column(db.String(3), nullable=False, default='no', server_default='no') #coluna de test migration

    # New instance instantiation procedure
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)