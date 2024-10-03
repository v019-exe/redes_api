import flask
from flask import Flask, request, jsonify
from Modules.binaries import binaries_bp
from Modules.redes import redes_bp
from Modules.gemini import gemini_bp

app = Flask(__name__)

app.register_blueprint(binaries_bp)
app.register_blueprint(redes_bp)
app.register_blueprint(gemini_bp)

@app.route('/')
def index():
    data = {
        "api": "ASIX CIBER",
        "version": "1.0.1",
        "author": "Jose Daniel",
        "description": "API de ASIX CIBER",
        "endpoints": {
            "binaries": {
                "convert_decimal_bin": "/api/binaries/convert_decimal_bin",
                "convert_bin_decimal": "/api/binaries/convert_bin_decimal",
                "convert_hex_bin": "/api/binaries/convert_hex_bin",
                "convert_bin_hex": "/api/binaries/convert_bin_hex",
                "convert_oct_bin": "/api/binaries/convert_oct_bin"
            },
            "redes": {
                "cidr_to_netmask": "/api/redes/cidr_to_netmask",
                "netmask_to_cidr": "/api/redes/netmask_to_cidr"
            },
            "gemini": {
                "chat": "/api/gemini/chat"
            }
        }
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
