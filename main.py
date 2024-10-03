import flask
from flask import Flask, request, jsonify
from Modules.binaries import binaries_bp
from Modules.redes import redes_bp

app = Flask(__name__)

app.register_blueprint(binaries_bp)
app.register_blueprint(redes_bp)

@app.route('/')
def index():
    return 'Bienvenido a la API de ASIX CIBER'

if __name__ == '__main__':
    app.run(debug=True)
