from base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields, post_load
from datetime import datetime

class BlogPost(Base):
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(DateTime)
    content = Column(String)
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    blog = relationship("Blog", back_populates="posts")

    def __repr__(self):
        return str(PageSchema().dumps(self).data)

class BlogPostSchema(Schema):
    id = fields.Int()
    title = fields.String()
    date = fields.Date()
    content = fields.String()

    @post_load
    def make_blog(self, data):
        return Page(**data)
