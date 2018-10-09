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
            url = urlparse(os.environ.get('DATABASE_URL', 'postgres://ktythxpeortqxa:872d1c6640d58dfcb8148f8e9e49b39b7331663716fce2d49c44c816456cf70e@ec2-54-83-29-34.compute-1.amazonaws.com:5432/d7jnd654md71uj'))
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

            try:
                cur = self.conn.cursor()
                cur.execute(query)
                id = cur.fetchone()[0]

                self.conn.commit()
                self.fechar()
                return id
            except (Exception, psycopg2.DatabaseError) as error:
                return None

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

    def deletar(self, query):
        self.conectar()

        if self.conn is not None:

            try:
                cur = self.conn.cursor()
                cur.execute(query)
                self.conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                return 0

        self.fechar()

        return 1