from flask import Blueprint, request
from services import page_service
from models.page import Page, PageSchema

page_api = Blueprint('page_api', __name__)

@page_api.route('/', methods=['GET'])
def all():
    return str(page_service.all())

@page_api.route('', methods=['POST'])
def create():
    json = request.get_json()
    page = PageSchema().load(request.get_json()).data
    return str(page_service.create(page))

@page_api.route('/<id>', methods=['GET'])
def get(id):
    page = page_service.get(id)
    return str(PageSchema().dumps(page).data)

@page_api.route('/<id>', methods=['POST'])
def update(id):
    json = request.get_json()
    page = PageSchema().load(request.get_json()).data
    return str(page_service.update(id, page))

@page_api.route('/find/<path:path>', methods=['GET'])
def find(path):
    if path[0] != '/':
        path = '/' + path
    page = page_service.find(path)
    return str(PageSchema().dumps(page).data)
