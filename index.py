import os
import json
from flask import Flask
from flask import request
from model import Mensagem

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/enviar")
def enviar_mensagem():
	usuario_id 	= request.args.get('usuario_id')
	texto 		= request.args.get('texto')

	retorno = {}
	if(usuario_id is None or texto is None):
		retorno["status"] = 0
		retorno["mensagem_status"] = "Parametros invalidos"
	else:		
		mensagem = Mensagem(usuario_id, texto)
		mensagem.salvar()

		if(mensagem.id is None):
			retorno["status"] = 0
			retorno["mensagem_status"] = "Mensagem nao enviada"

		else:
			retorno["status"] = 1
			retorno["mensagem_status"] = "Mensagem enviada"
			retorno["mensagem"] = mensagem.__dict__

	return json.dumps(retorno)

@app.route("/consultar")
def consultar_mensagem():
	id = request.args.get('id')

	retorno = {}
	if(id is None):
		retorno["status"] = 0
		retorno["mensagem_status"] = "Parametros invalidos"

	else:	
		mensagem = Mensagem.carregarPorId(id)
		if mensagem is None:
			retorno["status"] = 0
			retorno["mensagem_status"] = "Mensagem nao encontrada"

		else:
			retorno["status"] = 1
			retorno["mensagem_status"] = "Mensagem encontrada"
			retorno["mensagem"] = mensagem.__dict__
	return json.dumps(retorno)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)