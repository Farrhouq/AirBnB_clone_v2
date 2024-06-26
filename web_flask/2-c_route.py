#!/usr/bin/python3
"""This module starts a flask application"""

from flask import Flask
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    return "C " +  " ".join(text.split("_"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
