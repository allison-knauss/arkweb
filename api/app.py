from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *

@app.route('/health')
def health():
    return 'Ok'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
