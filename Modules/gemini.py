from flask import Blueprint, request, jsonify
import requests

gemini_bp = Blueprint('gemini', __name__)

class Gemini:
  @gemini_bp.route('/api/gemini/chat', methods=['POST'])
  def chat_gemini():
    text = request.args.get('text')
    if text is None:
      return jsonify({"error": "No se ha introducido texto"}), 400
    
    api_key = request.args.get("api_key")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"   
    headers = {
        "Content-Type": "application/json"
    }
    data = {"contents": [{"parts": [{"text": f"Ciberseguridad: {text}"}]}]}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 400:
        print("Clave API no valida")
    else:
        response_json = response.json()
        return response_json["candidates"][0]["content"]["parts"][0]["text"]

gemini = Gemini()
