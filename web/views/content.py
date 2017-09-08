from flask import render_template
from app import app
from clients import page_client
import base

@app.route('/<path:path>')
def content(path):
    page = page_client.find(path).json()
    if len(page) == 0:
        return render_template('404.html', nav=base.nav('/' + path))
    return render_template('content.html', nav=base.nav('/' + path), **page)
