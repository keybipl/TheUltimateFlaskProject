from flask import Flask, jsonify, request
import requests


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return f'<h1>Hello {name}, you are on the homepage!</h1>'


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h1>Hi {name}, you are from {location}. You are on the query page</h1>'


@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="Wyślij">
              </form>'''


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return f'Hello {name}, you are from {location}'


@app.route('/processjson', methods=['GET', 'POST'])
def processjson():
    response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
    data = response.json()
    kurs = data["rates"]
    lista = kurs[0]
    eur = lista['mid']
    kurs = float(eur)
    return f'Kurs: {kurs}'


if __name__ == '__main__':
    app.run()
