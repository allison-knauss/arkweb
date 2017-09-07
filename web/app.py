from flask import Flask
app = Flask(__name__)

@app.route('/')
def health():
    return '<h2>Ok</h2>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
