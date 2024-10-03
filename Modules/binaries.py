import time
from flask import Blueprint, request, jsonify

binaries_bp = Blueprint('binaries', __name__)

class Binaries:
  @binaries_bp.route('/api/binaries/convert_decimal_bin', methods=['GET'])
  def convert_decimal_bin():
      start = time.perf_counter()
      decimal = request.args.get('decimal')
      if decimal is None:
          return jsonify({"error": "No se ha introducido decimal"}), 400
      try:
          data = {
              'decimal': decimal,
              'bin': bin(int(decimal)).replace("0b", "")
          }
      except ValueError:
          return jsonify({"error": "El valor proporcionado no es un número válido"}), 400

      end = time.perf_counter()
      data["tiempo"] = f"{round((end - start) * 1000, 2)} ms"
      return jsonify(data), 200


  @binaries_bp.route('/api/binaries/convert_bin_decimal', methods=['GET'])
  def convert_bin_decimal():
    start = time.perf_counter()
    binary = request.args.get('bin')
    if binary is None:
      return jsonify({"error": "No se ha introducido binario"}), 400
    data = {
      "binario": binary,
      "decimal": int(binary, 2)
    }
    end = time.perf_counter()
    data["tiempo"] = f"{round((end - start) * 1000, 2)} ms"
    return jsonify(data), 200

  @binaries_bp.route('/api/binaries/convert_hex_bin', methods=['GET'])
  def convert_hex_bin():
    start = time.perf_counter()
    hex = request.args.get('hex')
    if hex is None:
      return jsonify({"error": "No se ha introducido hexadecimal"}), 400
    data = {
      'hex': hex,
      'bin': bin(int(hex, 16)).replace("0b", "")
    }
    end = time.perf_counter()
    data["tiempo"] = f"{round((end - start) * 1000, 2)} ms"
    return jsonify(data)

  @binaries_bp.route('/api/binaries/convert_bin_hex', methods=['GET'])
  def convert_bin_hex():
    start = time.perf_counter()
    bin = request.args.get('bin')
    if bin is None:
      return jsonify({"error": "No se ha introducido binario"}), 400
  
    data = {
      "binario": bin,
      "hexadecimal": hex(int(bin, 2)).replace("0x", "").upper() if bin else None,
    }
    end = time.perf_counter()
    data["tiempo"] = f"{round((end - start) * 1000, 2)} ms"
    return jsonify(data)

  @binaries_bp.route('/api/binaries/convert_oct_bin', methods=['GET'])
  def convert_oct_bin():
    start = time.perf_counter()
    oct = request.args.get('oct')
    if oct is None:
      return jsonify({"error": "No se ha introducido octal"}), 400
    data = {
      'oct': oct,
      'bin': bin(int(oct, 8)).replace("0b", "")
    }
    end = time.perf_counter()
    data["tiempo"] = f"{round((end - start) * 1000, 2)} ms"
    return jsonify(data)

binaries = Binaries()
