from repositories import page_repository

def all():
    return page_repository.all()

def create(page):
    return page_repository.create(page)

def get(id):
    return page_repository.get(id)

def update(id, page):
    return page_repository.update(id, page)

def find(path):
    return page_repository.find(path)
