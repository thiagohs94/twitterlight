from connection import Conexao

class Mensagem:
	def __init__(self, usuario_id, texto, id=None):
		self.id=id
		self.usuario_id = usuario_id
		self.texto = texto

	def salvar(self):
		query = "INSERT INTO mensagem(usuario_id, texto) VALUES ('" + self.usuario_id +"','" + self.texto + "') RETURNING id;"

		con = Conexao()
		id = con.inserir(query)

		self.id = id

	@staticmethod
	def carregarPorId(id):
		query = "SELECT usuario_id, texto, id FROM mensagem WHERE id = " + id;

		con = Conexao()
		result = con.carregar(query)

		if result is not None:
			return Mensagem(result[0][0], result[0][1], result[0][2])
		else:
			return None