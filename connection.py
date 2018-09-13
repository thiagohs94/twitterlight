import psycopg2
from config import config
    
class Conexao:
    def __init__(self):
        conn = None

    def conectar(self):
        try:
            params = config()
            self.conn = psycopg2.connect(**params)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.fechar()

    def fechar(self):
        if self.conn is not None:
            self.conn.close()

    def inserir(self, query):
        self.conectar()

        if self.conn is not None:
            cur = self.conn.cursor()
            cur.execute(query)
            id = cur.fetchone()[0]

            self.conn.commit()

        self.fechar()
        return id

    def carregar(self, query):
        self.conectar()

        if self.conn is not None:
            cur = self.conn.cursor()
            cur.execute(query)
            cont = cur.rowcount
            linhas = cur.fetchall()

        self.fechar()
        
        if(cont == 0):
            return None
        else:
            return linhas