import os
import psycopg2
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
    
class Conexao:
    def __init__(self):
        conn = None

    def conectar(self):
        try:
            url = urlparse(os.environ.get('DATABASE_URL', 'postgres://postgres:postgres@localhost:5432/mensagens'))
            db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
            self.conn   = psycopg2.connect(db)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.fechar()

    def fechar(self):
        if self.conn is not None:
            self.conn.close()

    def inserir(self, query):
        self.conectar()

        id = None
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