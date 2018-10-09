import os
import json
from flask import Flask
from flask import request
from flask_cors import CORS
from model import Mensagem

app = Flask(__name__)
CORS(app)

def obj_dict(obj):
    return obj.__dict__

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
		retorno["texto_status"] = "Parametros invalidos"
	else:		
		mensagem = Mensagem(usuario_id, texto)
		mensagem.salvar()

		if(mensagem.id is None):
			retorno["status"] = 0
			retorno["texto_status"] = "Mensagem nao enviada"

		else:
			retorno["status"] = 1
			retorno["texto_status"] = "Mensagem enviada"
			retorno["mensagem"] = mensagem.__dict__

	return json.dumps(retorno)

@app.route("/consultar")
def consultar_mensagem():
	id = request.args.get('id')

	retorno = {}
	if(id is None):
		retorno["status"] = 0
		retorno["texto_status"] = "Parametros invalidos"

	else:	
		mensagem = Mensagem.carregarPorId(id)
		if mensagem is None:
			retorno["status"] = 0
			retorno["texto_status"] = "Mensagem nao encontrada"

		else:
			retorno["status"] = 1
			retorno["texto_status"] = "Mensagem encontrada"
			retorno["mensagem"] = mensagem.__dict__
	return json.dumps(retorno)

@app.route("/consultarporusuario")
def consultar_mensagem_por_usuario():
	usuario_id = request.args.getlist('usuario_id')

	retorno = {}
	if(usuario_id is None):
		retorno["status"] = 0
		retorno["texto_status"] = "Parametros invalidos"

	else:	
		mensagens = Mensagem.carregarPorUsuariosIds(usuario_id)
		msgs = [ob.__dict__ for ob in mensagens]

		for m in msgs:

			#obter informacoes do usuario 
			url_consultar_user = os.environ.get('USER_PROFILE_URL', 'https://twitterlight-usuarios.herokuapp.com/consultar')
			url_consultar_user += "?usuario_id=" + usuario_id
			result = requests.get(url_consultar_user)
			result_json = json.loads(result.text)

			if(result_json["status"] == 1):
				m["usuario"] = result_json["usuario"]


		if mensagens is None:
			retorno["status"] = 0
			retorno["texto_status"] = "Nenhuma mensagem encontrada"

		else:
			retorno["status"] = 1
			retorno["texto_status"] = "Mensagens encontradas"
			retorno["mensagens"] = msgs
	return json.dumps(retorno)

@app.route("/info")
def info():
	mensagens = Mensagem.carregarTodos()

	retorno = "Mensagens (id, usuario_id, texto)"
	for m in mensagens:
		retorno += "<br/> " + str(m.id) + ", " + str(m.usuario_id) + ", " + str(m.texto)

	return retorno

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)