import requests

def all():
    r = requests.get('http://arkapi:5001/blog')
    return r

def paged(page=0):
    r = requests.get('http://arkapi:5001/blog/?page=' + str(page))
    return r
