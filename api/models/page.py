from base import Base
from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields, post_load

class Page(Base):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    path = Column(String)
    title = Column(String)
    content = Column(String)
    template = Column(String)

    def __repr__(self):
        return str(PageSchema().dumps(self).data)

class PageSchema(Schema):
    id = fields.Int()
    path = fields.String()
    title = fields.String()
    content = fields.String()
    template = fields.String()

    @post_load
    def make_user(self, data):
        return Page(**data)
