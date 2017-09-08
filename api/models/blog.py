from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields, post_load
from models.blog_post import BlogPostSchema

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    about = Column(String)
    posts = relationship("BlogPost", back_populates="blog")

    def __repr__(self):
        return str(PageSchema().dumps(self).data)

class BlogSchema(Schema):
    id = fields.Int()
    title = fields.String()
    description = fields.String()
    about = fields.String()
    posts = fields.Nested(BlogPostSchema, many=True)

    @post_load
    def make_blog(self, data):
        return Page(**data)
