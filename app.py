from flask import Flask, jsonify, request, url_for, redirect, session
import requests


app = Flask(__name__)

app.config['SECRET_KEY'] = '&Oc?P7zBQZ1H}7y{k!a?7oD>q)qHa'


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Przybyszu'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return f'<h1>Hello {name}, you are on the homepage!</h1>'


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h1>Hi {name}, you are from {location}. You are on the query page</h1>'


@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return '''<form method="POST" action="/theform">
                    <input type="text" name="name">
                    <input type="text" name="location">
                    <input type="submit" value="Wyślij">
                  </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        # return f'Hello {name}, you are from {location}'
        return redirect(url_for('home', name=name, location=location))



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
