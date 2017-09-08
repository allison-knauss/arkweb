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

    pageData = {
        'page': page,
        'blog': {}
    }

    return render_template(page['template'], nav=base.nav('/' + path), **pageData)
