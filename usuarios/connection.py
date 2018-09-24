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
            url = urlparse(os.environ.get('DATABASE_URL', 'postgres://ojhncwyfudbpyn:5f033208f304b047692f2eb06186efb53db96b950fb1294f432a7ff882826786@ec2-75-101-153-56.compute-1.amazonaws.com:5432/d7md6g02getn7i'))
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
                return 0

    def carregar(self, query):
        self.conectar()

        if self.conn is not None:
            cur = self.conn.cursor()
            cur.execute(query)
            cont = cur.rowcount
            if(cont > 0):
                linhas = cur.fetchall()
			
        self.fechar()

        if(cont == 0):
            return None
        else:
            return linhas
	
    def atualizar(self, query):
        self.conectar()

        if self.conn is not None:
            cur = self.conn.cursor()
            cur.execute(query)
            cont = cur.rowcount
			
        self.fechar()

    def deletar(self, query):
        self.conectar()

        if self.conn is not None:

            try:
                cur = self.conn.cursor()
                cur.execute(query)
                self.conn.commit()
                self.fechar()

                return 1   
            except (Exception, psycopg2.DatabaseError) as error:
                return 0

     