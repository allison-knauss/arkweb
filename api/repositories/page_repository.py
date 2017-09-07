from base_repository import session
from models.page import Page

def all():
    with session() as s:
        return [p for p in s.query(Page)]

def create(page):
    with session() as s:
        s.add(page)
        s.flush()
        s.refresh(page)
        return page.id

def get(id):
    with session() as s:
        return s.query(Page).filter_by(id=id).first()

def update(id, page):
    with session() as s:
        s.query(Page).filter_by(id=id).update({column: getattr(page, column) for column in Page.__table__.columns.keys()})
        return id

def find(path):
    with session() as s:
        return s.query(Page).filter_by(path=path).first()
