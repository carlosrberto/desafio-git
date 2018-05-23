from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/consulta-cep/")
def consulta_cep():
    cep = request.args.get("cep")
    if cep:
        r = requests.get('https://viacep.com.br/ws/'+ cep +'/json/')
        if r.status_code == 200:
            return jsonify(r.json())
        else: 
            return jsonify(error='invalid cep')
    else:
        return jsonify(error = 'cep is  required')
    
    