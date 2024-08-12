import psycopg2
from psycopg2 import sql

class AppDB:
    def __init__(self):
        self.conn = None
        self.cur = None
    
    def abrir_conexao(self):
        try:
            self.conn = psycopg2.connect(host="127.0.0.1", 
                                         port="5432", 
                                         database="Mercado", 
                                         user="postgres", 
                                         password="123")
        except (Exception, psycopg2.Error) as e:
            print("Erro ao conectar ao banco de dados", e)
            return None
    
    def encerrar_conexao(self):
        if self.conn:
            self.conn.close()
        
    def selecionar_dados(self):
        try:
            self.abrir_conexao()
            self.cur = self.conn.cursor()
            self.cur.execute(sql.SQL(('''SELECT * FROM "Produto"''')))
            rows = self.cur.fetchall()
            return rows

        except (Exception, psycopg2.Error) as e:
            print("Erro ao selecionar dados", e)

        finally:
            if self.conn:
                self.conn.close()

    def inserir_dados(self, nome, preco):
        try:
            self.abrir_conexao()
            self.cur = self.conn.cursor()
            self.cur.execute(sql.SQL('''INSERT INTO "Produto" (Nome, Preco) VALUES (%s, %s)''', (nome, preco)))
            self.conn.commit()
            self.cur.close()

        except (Exception, psycopg2.Error) as e:
            print("Erro ao inserir dados", e)

        finally:
            if self.conn:
                self.conn.close()
    
    def atualizar_dados(self, codigo, nome, preco):
        try:
            self.abrir_conexao()
            self.cur = self.conn.cursor()
            self.cur.execute(sql.SQL('''UPDATE "Produto" SET Nome = %s, Preco = %s WHERE Codigo = %s''', (nome, preco, codigo)))
            self.conn.commit()
            self.cur.close()

        except (Exception, psycopg2.Error) as e:
            print("Erro ao atualizar dados", e)

        finally:
            if self.conn:
                self.conn.close()

    def deletar_dados(self, codigo):
        try:
            self.abrir_conexao()
            self.cur = self.conn.cursor()
            self.cur.execute(sql.SQL('''DELETE FROM "Produto" WHERE Codigo = %s''', (codigo,)))
            self.conn.commit()
            self.cur.close()

        except (Exception, psycopg2.Error) as e:
            print("Erro ao deletar dados", e)

        finally:
            if self.conn:
                self.conn.close()

