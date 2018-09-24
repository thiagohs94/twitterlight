import os
import json
import requests
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

#recebe o id de um usuário e retorna todas as suas mensagens
@app.route("/posts")
def posts():
	usuario_id 	= request.args.get('usuario_id')

	url_mensagens_user = os.environ.get('USER_MESSAGES_URL', 'https://twitterlight-mensagens.herokuapp.com/consultarporusuario')
	url_mensagens_user += "?usuario_id=" + usuario_id
	result = requests.get(url_mensagens_user)
	result_json = json.loads(result.text)

	mensagens = None

	if(result_json["status"] == 1):
		mensagens = result_json["mensagens"]

	retorno = {}
	if mensagens is None:
		retorno["status"] = 0
		retorno["texto_status"] = "Nenhuma mensagem encontrada"

	else:
		retorno["status"] = 1
		retorno["texto_status"] = "Mensagens encontradas"
		retorno["mensagens"] = mensagens
	return json.dumps(retorno)

#recebe o id de um usuario e retorna todas as suas mensagens e dos usuários que ele segue
@app.route("/home")
def home():
	usuario_id = request.args.get('usuario_id')

	retorno = {}
	if(usuario_id is None):
		retorno["status"] = 0
		retorno["texto_status"] = "Parametros invalidos"
	else:

		url_perfil_user = os.environ.get('USER_PROFILE_URL', 'https://twitterlight-mensagens.herokuapp.com/consultarporusuario')
		url_mensagens_user += "?usuario_id=" + usuario_id
		result = requests.get(url_mensagens_user)
		result_json = json.loads(result.text)

		mensagens = None

	#TODO



	#else:	
		#mensagem = Mensagem.carregarPorId(id)
		#if mensagem is None:
		#	retorno["status"] = 0
		#	retorno["texto_status"] = "Mensagem nao encontrada"

		#else:
		#	retorno["status"] = 1
		#	retorno["texto_status"] = "Mensagem encontrada"
		#	retorno["mensagem"] = mensagem.__dict__
	return json.dumps(retorno)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)