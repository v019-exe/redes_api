import flask
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenido a la API de ASIX CIBER'

if __name__ == '__main__':
    app.run(debug=True)
