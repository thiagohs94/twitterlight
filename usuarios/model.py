from connection import Conexao

class User:
	def __init__(self, username, senha, nome=None , bio=None ,id=None):
		self.id=id
		self.username = username
		self.senha = senha
		self.nome = nome
		self.bio = bio

	def salvar(self):
		query = "INSERT INTO Users(username, senha, nome, bio) VALUES ('" + self.username +"','" + self.senha + "','" + self.nome + "','" + self.bio + "') RETURNING id;"

		con = Conexao()
		id = con.inserir(query)

		self.id = id

	def deletar(self):
		query = "DELETE FROM Users WHERE id = " + str(self.id) + ";"

		con = Conexao()
		result = con.deletar(query)

		return result

	@staticmethod
	def buscarPorId(id):
		query = "SELECT username, senha, nome, bio, id FROM Users WHERE id = " + str(id)

		con = Conexao()
		result = con.carregar(query)

 		if result is not None:
			return User(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])
		else:
			return None

	@staticmethod
	def buscarMuitosPorId(ids):
		query = "SELECT username, senha, nome, bio, id FROM Users WHERE "

		for i,usuario_id in enumerate(ids,start=0):
			if(i==0):
				query += "id=" + str(usuario_id) + " "
			else:
				query += "OR id=" + str(usuario_id) + " "

		con = Conexao()
		result = con.carregar(query)

		retorno = []
		if result is not None:
			for r in result:
				retorno.append(User(r[0], r[1], r[2], r[3], r[4] ))
			return retorno
		else:
			return None

	@staticmethod
	def buscarTodos():
		query = "SELECT username, senha, nome, bio, id FROM Users;"

		con = Conexao()
		result = con.carregar(query)

		retorno = []
		if result is not None:
			for r in result:
				retorno.append(User(r[0], r[1], r[2], r[3], r[4]))
			return retorno
		else:
			return None
			
	@staticmethod
	def atualizarNome(id, nome):
		update = "UPDATE Users SET nome = '" + nome + "' WHERE id = " + str(id) + ';';
		query = "SELECT username, senha, nome, bio, id FROM Users WHERE id = " + str(id) + ';';

		con = Conexao()
		con.carregar(update)
		result = con.carregar(query)

		if result is not None:
			return User(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4] )
		else:
			return None
			
	@staticmethod
	def atualizarBio(id, bio):
		update = "UPDATE Users SET bio = '" + bio + "' WHERE id = " + str(id) + ';';
		query = "SELECT username, senha, nome, bio, id FROM Users WHERE id = " + str(id) + ';';

		con = Conexao()
		con.carregar(update)
		result = con.carregar(query)

		if result is not None:
			return User(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4] )
		else:
			return None



class Seguidores:
	def __init__(self, seguidor=None, seguido=None, numSeguidores=None , numSeguindo=None, id=None):
		self.seguidor = seguidor
		self.seguido = seguido
		self.numSeguidores = numSeguidores
		self.numSeguindo = numSeguindo
		self.id = id;

	def salvar(self):
		query = "INSERT INTO Seguidores(idseguidor, idseguido) VALUES ('" + str(self.seguidor) +"','" + str(self.seguido) + "') RETURNING id;"

		con = Conexao()
		id = con.inserir(query)

		self.id = id

	def deletar(self):
		query = "DELETE FROM Seguidores WHERE idseguidor = " + str(self.seguidor) + " AND idseguido = " + str(self.seguido) + ";"

		con = Conexao()
		result = con.deletar(query)

		return result
	
	@staticmethod
	def numSeguidores(id):
		querySeguidor = "SELECT COUNT (*) FROM Seguidores WHERE idseguidor = " + id + ';';
		querySeguido = "SELECT COUNT (*) FROM Seguidores WHERE idseguido = " + id + ';';
		
		seg = Seguidores()

		con = Conexao()
		result1 = con.carregar(querySeguidor)
		result2 = con.carregar(querySeguido)
		
		if result1 is not None and result2 is not None:
			seg.numSeguindo = result1
			seg.numSeguidores = result2
			return seg
		else:
			return None

	@staticmethod
	def buscar(id_seguidor, id_seguido):
		query = "SELECT idseguidor, idseguido FROM Seguidores WHERE idseguidor = " + str(id_seguidor) + " AND idseguido = " + str(id_seguido) +";"

		con = Conexao()
		result = con.carregar(query)

		if result is not None:
			return Seguidores(result[0][0], result[0][1])
		else:
			return None

	@staticmethod
	def buscarPorIdSeguidor(id_seguidor):
		query = "SELECT idseguidor, idseguido FROM Seguidores WHERE idseguidor = " + str(id_seguidor) +";"

		con = Conexao()
		result = con.carregar(query)

		retorno = []
		if result is not None:
			for r in result:
				retorno.append(Seguidores(r[0], r[1]))
			return retorno
		else:
			return None

	@staticmethod
	def buscarTodos():
		query = "SELECT idseguidor, idseguido, id FROM Seguidores;"

		con = Conexao()
		result = con.carregar(query)

		retorno = []
		if result is not None:
			for r in result:
				retorno.append(Seguidores(r[0], r[1], None, None, r[2]))
			return retorno
		else:
			return None
