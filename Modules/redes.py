from flask import Blueprint, request, jsonify
import ipaddress

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

  @redes_bp.route("/api/redes/get-class", methods=["GET"])
  def get_class():
    ip = request.args.get("ip")
    if ip is None:
      return jsonify({"error": "No se ha introducido IP"}), 400
    
    splitted_ip = ip.split(".")
    if 1 <= int(splitted_ip[0]) <= 127 and 0 <= int(splitted_ip[1]) <= 255:
                    data = {
                        "Clase": "A",
                        "Default Mask": "255.0.0.0"
                    }
    elif 128 <= int(splitted_ip[0]) <= 191 and 0 <= int(splitted_ip[1]) <= 255:
                    data = {
                        "Clase": "B",
                        "Default Mask": "255.255.0.0"
                    }
    elif 192 <= int(splitted_ip[0]) <= 223 and 0 <= int(splitted_ip[1]) <= 255:
                    data = {
                        "Clase": "C",
                        "Default Mask": "255.255.255.0"
                    }
    else:
                    data = {
                        "Error": "Dirección IP fuera de los rangos conocidos"
                    }
                    return jsonify(data), 400

    return jsonify(data), 200
  
  @redes_bp.route("/api/redes/subnets", methods=["GET"])
  @redes_bp.route("/api/redes/subnets", methods=["GET"])
  def subnets():
      ip = request.args.get("ip")
      if ip is None:
          return jsonify({"error": "No se ha introducido IP"}), 400

      mask = request.args.get("mask")
      if mask is None:
          return jsonify({"error": "No se ha introducido mask"}), 400

      new_prefix = request.args.get("new_prefix")
      
      try:
          
          network = ipaddress.ip_network(f"{ip}/{mask}", strict=False)
      except ValueError:
          return jsonify({"error": "IP o máscara inválida"}), 400


      first_octet = int(ip.split(".")[0])
      if first_octet < 128:
          ip_class = "A"
      elif first_octet < 192:
          ip_class = "B"
      elif first_octet < 224:
          ip_class = "C"
      else:
          ip_class = "No soportado"

      
      try:
          if new_prefix:
              new_prefix = int(new_prefix)

              subnets = [{
                  "subred": str(subnet.network_address),
                  "rango": f"{subnet.network_address + 1} - {subnet.broadcast_address - 1}",
                  "broadcast": str(subnet.broadcast_address)
              } for subnet in network.subnets(new_prefix=new_prefix)]
          else:
            
              subnets = [{
                  "subred": str(subnet.network_address),
                  "rango": f"{subnet.network_address + 1} - {subnet.broadcast_address - 1}",
                  "broadcast": str(subnet.broadcast_address)
              } for subnet in network.subnets()]
      except ValueError:
          return jsonify({"error": "Prefijo inválido"}), 400

      return jsonify({
          "ip": ip,
          "mask": mask,
          "clase": ip_class,
          "subredes": subnets
      })
        
redes = Redes()
