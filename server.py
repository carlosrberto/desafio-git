from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/consulta-cep/")
def consulta_cep():
    cep = request.args.get("cep")
    
    r = requests.get('https://viacep.com.br/ws/'+ cep +'/json/')
    return jsonify(r.json())
    