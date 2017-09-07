from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='/static')

from views import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
