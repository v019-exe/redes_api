from flask import Blueprint, request, jsonify

redes_bp = Blueprint('redes', __name__)

class Redes:
  @redes_bp.route('/api/redes/cidr_to_netmask', methods=['GET'])
  def cidr_to_netmask():
    cidr = request.args.get('cidr')
    if cidr is None:
      return jsonify({"error": "No se ha introducido CIDR"}), 400
    cidrs = {
      "/8": "255.0.0.0",
      "/9": "255.128.0.0",
      "/10": "255.192.0.0",
      "/11": "255.224.0.0",
      "/12": "255.240.0.0",
      "/13": "255.248.0.0",
      "/14": "255.252.0.0",
      "/15": "255.254.0.0",
      "/16": "255.255.0.0",
      "/17": "255.255.128.0",
      "/18": "255.255.192.0",
      "/19": "255.255.224.0",
      "/20": "255.255.240.0",
      "/21": "255.255.248.0",
      "/22": "255.255.252.0",
      "/23": "255.255.254.0",
      "/24": "255.255.255.0",
      "/25": "255.255.255.128",
      "/26": "255.255.255.192",
      "/27": "255.255.255.224",
      "/28": "255.255.255.240",
      "/29": "255.255.255.248",
      "/30": "255.255.255.252",
      "/31": "255.255.255.254",
      "/32": "255.255.255.255"
    }

    for key,value in cidrs.items():
      if cidr.startswith(key):
        data = {
          "cidr": cidr,
          "netmask": value
        }
        return jsonify(data), 200
    return jsonify({"error": "No se ha encontrado una CIDR válida"}), 400

  @redes_bp.route('/api/redes/netmask_to_cidr', methods=['GET'])
  def netmask_to_cidr():
    cidrs_invertido = {
      "255.0.0.0": "/8",
      "255.128.0.0": "/9",
      "255.192.0.0": "/10",
      "255.224.0.0": "/11",
      "255.240.0.0": "/12",
      "255.248.0.0": "/13",
      "255.252.0.0": "/14",
      "255.254.0.0": "/15",
      "255.255.0.0": "/16",
      "255.255.128.0": "/17",
      "255.255.192.0": "/18",
      "255.255.224.0": "/19",
      "255.255.240.0": "/20",
      "255.255.248.0": "/21",
      "255.255.252.0": "/22",
      "255.255.254.0": "/23",
      "255.255.255.0": "/24",
      "255.255.255.128": "/25",
      "255.255.255.192": "/26",
      "255.255.255.224": "/27",
      "255.255.255.240": "/28",
      "255.255.255.248": "/29",
      "255.255.255.252": "/30",
      "255.255.255.254": "/31",
      "255.255.255.255": "/32"
    }

    netmask = request.args.get('netmask')
    if netmask is None:
      return jsonify({"error": "No se ha introducido netmask"}), 400
    for key,value in cidrs_invertido.items():
      if netmask == key:
        data = {
          "netmask": netmask,
          "cidr": value
        }
        return jsonify(data), 200
    return jsonify({"error": "No se ha encontrado una netmask válida"}), 400

redes = Redes()
