import os
import json
from flask import Flask
from flask import request
from model import User
from model import Seguidores

app = Flask(__name__)

def obj_dict(obj):
    return obj.__dict__

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/cadastro")
def cadastrar_usuario():
	username 	= request.args.get('username')
	senha 		= request.args.get('senha')
	nome 		= request.args.get('nome')
	bio 		= request.args.get('bio')

	retorno = {}
	if(username is None or senha is None or nome is None or bio is None):
		retorno["status"] = 0
		retorno["texto_status"] = "Parametros invalidos"
	else:		
		user = User(username, senha, nome, bio)
		user.salvar()

		if(user.id is None):
			retorno["status"] = 0
			retorno["texto_status"] = "Usuario nao cadastrado"

		else:
			retorno["status"] = 1
			retorno["texto_status"] = "Usuario cadastrado"
			retorno["usuario"] = user.__dict__

	return json.dumps(retorno)


@app.route("/remover")
def remover_usuario():
	id = request.args.get('usuario_id')

	retorno = {}
	if(id is None):
		retorno["status"] = 0
		retorno["texto_status"] = "Parametros invalidos"

	else:

		user = User.buscarPorId(id)
		if user is None:
			retorno["status"] = 0
			retorno["texto_status"] = "Usuario nao encontrado"
		
		else:
			r = user.deletar()
			if(r == 0):
				retorno["status"] = 0
				retorno["texto_status"] = "Erro ao remover usuario"
			else:
				retorno["status"] = 1
				retorno["texto_status"] = "Usuario removido"
			
	return json.dumps(retorno)

@app.route("/seguir")
def seguir():
	seguidor = request.args.get('seguidor')
	seguido = request.args.get('seguido')

	retorno = {}
	if(seguidor is None or seguido is None):
		retorno["status"] = 0
		retorno["texto_status"] = "Parametros invalidos"

	else:	
		seg = Seguidores(seguidor, seguido)
		seg.salvar()
		
		if seg.id is None:
			retorno["status"] = 0
			retorno["texto_status"] = "Erro"

		else:
			retorno["status"] = 1
			retorno["texto_status"] = "Seguindo"
			retorno["usuario"] = seg.__dict__
	return json.dumps(retorno) 

@app.route("/pararseguir")
def parar_seguir():
	seguidor = request.args.get('seguidor')
	seguido = request.args.get('seguido')

	retorno = {}
	if(seguidor is None or seguido is None):
		retorno["status"] = 0
		retorno["texto_status"] = "Parametros invalidos"

	else:

		seg = Seguidores.buscar(seguidor,seguido)
		if seg is None:
			retorno["status"] = 0
			retorno["texto_status"] = "relacao nao encontrada"
		
		else:
			r = seg.deletar()
			if(r == 0):
				retorno["status"] = 0
				retorno["texto_status"] = "Erro ao remover relacao"
			else:
				retorno["status"] = 1
				retorno["texto_status"] = "Relacao removida"
			
	return json.dumps(retorno)


@app.route("/perfil")
def perfil():
	usuario_id = request.args.get('usuario_id')

	retorno = {}
	if(usuario_id is None):
		retorno["status"] = 0
		retorno["texto_status"] = "Parametros invalidos"	

	else:	
		user = User.buscarPorId(usuario_id)
		seg = Seguidores.numSeguidores(usuario_id)
		
		
		if user is None:
			retorno["status"] = 0
			retorno["user_status"] = "Usuario nao encontrado"

		else:

			seguindo = Seguidores.buscarPorIdSeguidor(user.id)

			retorno["status"] = 1
			retorno["user_status"] = "Usuario encontrado"
			retorno["usuario"] = user.__dict__
			retorno["numero_seguindo"] = seg.numSeguindo
			retorno["numero_seguidores"] = seg.numSeguidores
			retorno["seguindo"] = [ob.seguido for ob in seguindo]
	return json.dumps(retorno)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)