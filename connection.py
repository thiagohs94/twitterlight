import os
import psycopg2
from config import config
    
class Conexao:
    def __init__(self):
        conn = None

    def conectar(self):
        try:
            host        = os.environ.get('DB_HOST', 'localhost')
            database    = os.environ.get('DB_DATABASE', 'mensagens')
            user        = os.environ.get('DB_USER', 'postgres')
            password    = os.environ.get('DB_PASSWORD', 'postgres')
            self.conn   = psycopg2.connect(host=host, database=database, user=user, password=password)
            
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