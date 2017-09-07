import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base

SQLALCHEMY_ENGINE_URI = os.environ['SQLALCHEMY_ENGINE_URI']
SQLALCHEMY_DATABASE = os.environ['SQLALCHEMY_DATABASE']
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_ENGINE_URI + '/' + SQLALCHEMY_DATABASE

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Session = sessionmaker(bind=engine)

from contextlib import contextmanager

@contextmanager
def session():
    s = Session()
    try:
        yield s
    except Exception, ex:
        s.rollback()
        raise Exception(ex)
    s.commit()

