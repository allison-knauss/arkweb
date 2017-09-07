import os

SQLALCHEMY_ENGINE_URI = os.environ['SQLALCHEMY_ENGINE_URI']
SQLALCHEMY_DATABASE = os.environ['SQLALCHEMY_DATABASE']
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_ENGINE_URI + '/' + SQLALCHEMY_DATABASE
SQLALCHEMY_MIGRATE_REPO = os.environ['SQLALCHEMY_MIGRATE_REPO']
SQLALCHEMY_TRACK_MODIFICATIONS = True

