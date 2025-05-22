from storage.database_connect import DatabaseConnection

db = DatabaseConnection()

def authenticate_user(email, password):
    """Autentica um usuário"""
    query = "SELECT id, name, email, phone FROM users WHERE email = %s AND password = %s"
    result = db.fetch_one(query, (email, password))
    if result:
        return True, {
            'id': result[0],      # id está no índice 0
            'name': result[1],    # nome está no índice 1
            'email': result[2],   # email está no índice 2
            'phone': result[3]    # telefone está no índice 3
        }
    return False, "Credenciais inválidas"

def register_user(user_id, name, email, password):
    """Registra um novo usuário"""
    # Primeiro verifica se o email já existe
    check_query = "SELECT id FROM users WHERE email = %s"
    if db.fetch_one(check_query, (email,)):
        return False, "Email já registrado"
    
    query = """
    INSERT INTO users (id, name, email, password, phone)
    VALUES (%s, %s, %s, %s, NULL)
    """
    success, message = db.execute_query(query, (user_id, name, email, password))
    if success:
        return True, "Usuário registrado com sucesso"
    return False, message

def get_user_by_id(user_id):
    """Retorna os dados do usuário pelo ID"""
    query = "SELECT id, name, email, phone FROM users WHERE id = %s"
    result = db.fetch_one(query, (user_id,))
    if result:
        return {
            'id': result[0],
            'name': result[1],
            'email': result[2],
            'phone': result[3]
        }
    return None

def get_user_credentials(user_id):
    """Retorna as credenciais do usuário"""
    query = "SELECT name, email, password, phone FROM users WHERE id = %s"
    result = db.fetch_one(query, (user_id,))
    if result:
        return result[0], result[1], result[2], result[3]
    return None, None, None, None

def update_user(user_id, name=None, email=None, phone=None):
    """Atualiza os dados do usuário"""
    if not any([name, email, phone]):
        return False, "Nenhum dado para atualizar"
    
    updates = []
    params = []
    
    if name:
        updates.append("name = %s")
        params.append(name)
    if email:
        # Verifica se o email já existe
        check_query = "SELECT id FROM users WHERE email = %s AND id != %s"
        if db.fetch_one(check_query, (email, user_id)):
            return False, "Email já registrado"
        updates.append("email = %s")
        params.append(email)
    if phone:
        updates.append("phone = %s")
        params.append(phone)
    
    params.append(user_id)
    query = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
    return db.execute_query(query, params)

def load_transactions(user_id):
    """Carrega as transações de um usuário específico"""
    query = """
        SELECT 
            type, amount, description, category, 
            TO_CHAR(date, 'DD/MM/YYYY HH24:MI') as formatted_date
        FROM transactions 
        WHERE user_id = %s 
        ORDER BY date DESC
    """
    results = db.fetch_all(query, (user_id,))
    if not results:
        return []
    
    return [
        {
            'type': row[0],
            'value': float(row[1]),
            'description': row[2],
            'category': row[3],
            'date': row[4]
        }
        for row in results
    ]

def save_transactions(transaction_data):
    """Salva uma nova transação"""
    query = """
        INSERT INTO transactions 
        (user_id, type, amount, description, category)
        VALUES (%s, %s, %s, %s, %s)
    """
    
    # Converte 'value' para 'amount' para corresponder ao schema do banco
    amount = transaction_data.get('value', 0.0)
    
    params = (
        transaction_data.get('user_id'),
        transaction_data.get('type'),
        amount,
        transaction_data.get('description'),
        transaction_data.get('category')
    )
    
    try:
        success, message = db.execute_query(query, params)
        if success:
            print("✅ Transação salva com sucesso!")
            return True, "Transação salva com sucesso"
        return False, message
    except Exception as e:
        error_msg = f"Erro ao salvar transação: {str(e)}"
        print(f"❌ {error_msg}")
        return False, error_msg

def get_transaction_summary(user_id):
    """Retorna um resumo das transações do usuário"""
    query = """
        SELECT 
            type,
            SUM(amount) as total,
            COUNT(*) as count
        FROM transactions 
        WHERE user_id = %s 
        GROUP BY type
    """
    results = db.fetch_all(query, (user_id,))
    if not results:
        return {
            'receitas': 0.0,
            'despesas': 0.0,
            'total_receitas': 0,
            'total_despesas': 0
        }
    
    summary = {
        'receitas': 0.0,
        'despesas': 0.0,
        'total_receitas': 0,
        'total_despesas': 0
    }
    
    for row in results:
        tipo, valor, quantidade = row
        if tipo == 'receita':
            summary['receitas'] = float(valor)
            summary['total_receitas'] = quantidade
        else:
            summary['despesas'] = float(valor)
            summary['total_despesas'] = quantidade
    
    return summary