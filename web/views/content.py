from flask import render_template
from app import app
from clients import page_client
import base

@app.route('/<path:path>')
def content(path):
    pageData = page_client.find(path)
    if pageData == None or pageData.text == '{}':
        return render_template('404.html', nav=base.nav('/' + path))
    page = pageData.json()
    return render_template('content.html', nav=base.nav('/' + path), **page)
