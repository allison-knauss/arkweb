from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    title = 'arkweb'
    welcome = "Welcome to Allison's Personal Website"
    return render_template('index.html', title=title, welcome=welcome)
