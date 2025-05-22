import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        """Inicializa a conexão com o banco de dados"""
        self.config = {
            'host': os.getenv('NEON_HOST'),
            'database': os.getenv('NEON_NAME'),
            'user': os.getenv('NEON_USER'),
            'password': os.getenv('NEON_PASSWORD'),
            'sslmode': 'require'
        }

    def connect(self):
        """Estabelece uma conexão com o banco de dados"""
        try:
            return psycopg2.connect(**self.config)
        except Exception as e:
            print(f"❌ Erro ao conectar ao banco de dados: {e}")
            return None

    def execute_query(self, query, params=None):
        """Executa uma query SQL e retorna sucesso/falha com mensagem"""
        connection = self.connect()
        if not connection:
            return False, "Falha ao conectar ao banco de dados"
        
        try:
            cursor = connection.cursor()
            cursor.execute(query, params or ())
            connection.commit()
            return True, "Operação realizada com sucesso"
        except Exception as e:
            return False, str(e)
        finally:
            cursor.close()
            connection.close()

    def fetch_one(self, query, params=None):
        """Executa uma query SELECT e retorna uma única linha"""
        connection = self.connect()
        if not connection:
            return None
        
        try:
            cursor = connection.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchone()
        except Exception as e:
            print(f"❌ Erro ao executar query: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

    def fetch_all(self, query, params=None):
        """Executa uma query SELECT e retorna todas as linhas"""
        connection = self.connect()
        if not connection:
            return []
        
        try:
            cursor = connection.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except Exception as e:
            print(f"❌ Erro ao executar query: {e}")
            return []
        finally:
            cursor.close()
            connection.close()