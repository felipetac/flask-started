import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 

class Config(object):

    # Statement for enabling the development environment
    DEBUG = False

    TESTING = False

    # Define the database - we are working with
    # SQLite for this example
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = False

    # Use a secure, unique and absolutely secret key for
    # signing the data. 
    #CSRF_SESSION_KEY = "secret"

    # JWT Secret key
    SECRET_KEY = "25ef26bae776093bb5ff6ff9aa3a27dcc83d3b5c188d624d"

    # JWT Algorithm
    JWT_ALGORITHM = 'HS512'

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

class TestingConfig(Config):
    TESTING = True