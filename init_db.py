from storage.database_connect import DatabaseConnection

def create_tables():
    db = DatabaseConnection()

    create_users = """
        CREATE TABLE IF NOT EXISTS users (
            id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            phone VARCHAR(20)
        );
    """

    create_transactions = """
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            user_id VARCHAR(36) REFERENCES users(id),
            type VARCHAR(10) NOT NULL,
            amount DECIMAL(10,2) NOT NULL,
            description TEXT,
            category VARCHAR(50),
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """

    success, message = db.execute_query(create_users)
    if success:
        print("✅ Tabela de usuários criada com sucesso.")
    else:
        print(f"❌ Erro ao criar tabela de usuários: {message}")

    success, message = db.execute_query(create_transactions)
    if success:
        print("✅ Tabela de transações criada com sucesso.")
    else:
        print(f"❌ Erro ao criar tabela de transações: {message}")

if __name__ == "__main__":
    print("Iniciando criação das tabelas...")
    create_tables()
    print("Processo finalizado.")