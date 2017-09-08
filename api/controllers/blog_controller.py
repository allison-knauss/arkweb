from flask import Blueprint, request
from services import blog_service
from models.blog import Blog, BlogSchema

blog_api = Blueprint('blog_api', __name__)

@blog_api.route('/', methods=['GET'])
def all():
    requestedPage = int(request.args.get('page'))
    blog = blog_service.page(requestedPage)
    if blog is None:
        return {}
    return BlogSchema().dumps(blog).data

