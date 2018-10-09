from connection import Conexao

class Mensagem:
	def __init__(self, usuario_id, texto, id=None):
		self.id=id
		self.usuario_id = usuario_id
		self.texto = texto

	def salvar(self):
		query = "INSERT INTO mensagem(usuario_id, texto) VALUES ('" + str(self.usuario_id) +"','" + self.texto + "') RETURNING id;"

		con = Conexao()
		id = con.inserir(query)

		self.id = id

	@staticmethod
	def carregarPorId(id):
		query = "SELECT usuario_id, texto, id FROM mensagem WHERE id = " + str(id);

		con = Conexao()
		result = con.carregar(query)

		if result is not None:
			return Mensagem(result[0][0], result[0][1], result[0][2])
		else:
			return None

	@staticmethod
	def carregarPorUsuariosIds(usuarios_ids):
		query = "SELECT usuario_id, texto, id FROM mensagem ";

		for i,usuario_id in enumerate(usuarios_ids,start=0):
			if(i==0):
				query += "WHERE usuario_id=" + str(usuario_id) + " ";
			else:
				query += "OR usuario_id=" + str(usuario_id) + " ";

		query += "ORDER BY id"

		con = Conexao()
		result = con.carregar(query)

		retorno = []
		if result is not None:
			for r in result:
				retorno.append(Mensagem(r[0], r[1], r[2]))
			return retorno
		else:
			return None

	@staticmethod
	def carregarTodos():
		query = "SELECT usuario_id, texto, id FROM mensagem;"

		con = Conexao()
		result = con.carregar(query)

		retorno = []
		if result is not None:
			for r in result:
				retorno.append(Mensagem(r[0], r[1], r[2]))
			return retorno
		else:
			return None