from flask import render_template
from app import app
from clients import page_client
import base

@app.route('/')
@app.route('/index')
def index():
    title = 'ARK'
    welcome = 'Welcome!'
    return render_template('index.html', nav=base.nav('/'), title=title, welcome=welcome)

