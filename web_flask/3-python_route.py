#!/usr/bin/python3

''' a script that starts a Flask web application '''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    ''' function that returns "Hello HBNB" '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    ''' function that returns "HBNB" '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    ''' functions that handles variable '''
    if '_' in text:
        new_text = text.replace('_', ' ')
        return f'C {new_text}'
    else:
        return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_route(text='is cool'):
    ''' functions that handles variable '''
    if '_' in text:
        new_text = text.replace('_', ' ')
        return f'Python {new_text}'
    else:
        return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
