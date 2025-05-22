import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_to_database():
    """
    Conecta ao banco de dados PostgreSQL usando as variáveis de ambiente.
    """
    try:
        connection = psycopg2.connect(
            host=os.getenv('NEON_HOST'),
            database=os.getenv('NEON_NAME'),
            user=os.getenv('NEON_USER'),
            password=os.getenv('NEON_PASSWORD'),
            sslmode='require'
        )
        return connection
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        return None


def close_connection(connection):
    """
    Fecha a conexão com o banco de dados.
    """
    if connection:
        connection.close()
        print("🔌 Conexão com o banco de dados fechada.")


def execute_query(query, params=None):
    """
    Executa comandos SQL que não retornam dados (INSERT, UPDATE, DELETE, CREATE).
    """
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            connection.commit()
            print("✅ Query executada com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao executar a query: {e}")
        finally:
            cursor.close()
            close_connection(connection)


def fetch_query(query, params=None):
    """
    Executa SELECT e retorna os resultados.
    """
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"❌ Erro ao executar o SELECT: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)
    return None


