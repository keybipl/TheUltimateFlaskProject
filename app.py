from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return f'<h1>Hello {name}, you are on the homepage!</h1>'


if __name__ == '__main__':
    app.run()
