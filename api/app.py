from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/health')
def health():
    return 'Ok'

from controllers.page_controller import page_api
app.register_blueprint(page_api, url_prefix='/page')
from controllers.blog_controller import blog_api
app.register_blueprint(blog_api, url_prefix='/blog')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
