import requests

def all():
    r = requests.get('http://arkapi:5001/page')
    return r

def find(path):
    r = requests.get('http://arkapi:5001/page/find/' + path)
    return r
