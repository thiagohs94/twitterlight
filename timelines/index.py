import os
import json
import requests
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/posts")
def posts():
	usuario_id 	= request.args.get('usuario_id')

	url_mensagens_user = os.environ.get('USER_MESSAGES_URL', 'https://twitterlight-mensagens.herokuapp.com/consultarporusuario')
	url_mensagens_user += "?usuario_id=" + usuario_id
	result = requests.get(url_mensagens_user).content

	return result

	retorno = {}
	if(usuario_id is None):
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

@app.route("/home")
def home():
	usuario_id = request.args.get('usuario_id')

	retorno = {}
	if(usuario_id is None):
		retorno["status"] = 0
		retorno["mensagem_status"] = "Parametros invalidos"

	#else:	
		#mensagem = Mensagem.carregarPorId(id)
		#if mensagem is None:
		#	retorno["status"] = 0
		#	retorno["mensagem_status"] = "Mensagem nao encontrada"

		#else:
		#	retorno["status"] = 1
		#	retorno["mensagem_status"] = "Mensagem encontrada"
		#	retorno["mensagem"] = mensagem.__dict__
	return json.dumps(retorno)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)