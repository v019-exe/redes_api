from flask import Blueprint, request, jsonify

binaries_bp = Blueprint('binaries', __name__)

class Binaries:
  @binaries_bp.route('/convert_decimal_bin', methods=['GET'])
  def convert_decimal_bin():
    decimal = request.args.get('decimal')
    if decimal is None:
      return jsonify({"error": "No se ha introducido decimal"}), 400
    data = {
      'decimal': decimal,
      'bin': bin(int(decimal)).replace("0b", "")
    }
    return jsonify(data), 200

  @binaries_bp.route('/convert_bin_decimal', methods=['GET'])
  def convert_bin_decimal():
    binary = request.args.get('bin')
    if binary is None:
      return jsonify({"error": "No se ha introducido binario"}), 400
    data = {
      "binario": binary,
      "decimal": int(binary, 2)
    }
    return jsonify(data), 200

  @binaries_bp.route('/convert_hex_bin', methods=['GET'])
  def convert_hex_bin():
    hex = request.args.get('hex')
    if hex is None:
      return jsonify({"error": "No se ha introducido hexadecimal"}), 400
    data = {
      'hex': hex,
      'bin': bin(int(hex, 16)).replace("0b", "")
    }
    return jsonify(data)

  @binaries_bp.route('/convert_bin_hex', methods=['GET'])
  def convert_bin_hex():
    bin = request.args.get('bin')
    if bin is None:
      return jsonify({"error": "No se ha introducido binario"}), 400
  
    data = {
      "binario": bin,
      "hexadecimal": hex(int(bin, 2)).replace("0x", "").upper() if bin else None,
    }
    return jsonify(data)

  @binaries_bp.route('/convert_oct_bin', methods=['GET'])
  def convert_oct_bin():
    oct = request.args.get('oct')
    if oct is None:
      return jsonify({"error": "No se ha introducido octal"}), 400
    data = {
      'oct': oct,
      'bin': bin(int(oct, 8)).replace("0b", "")
    }
    return jsonify(data)

binaries = Binaries()
