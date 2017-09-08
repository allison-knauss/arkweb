from base_repository import session
from models.blog import Blog
from models.blog_post import BlogPost

def page(page, per_page=2):
    with session() as s:
        blog = s.query(Blog).first()
        blog.posts = s.query(BlogPost).order_by(BlogPost.date.desc()).limit(per_page).offset(page*per_page).all()
        return blog

