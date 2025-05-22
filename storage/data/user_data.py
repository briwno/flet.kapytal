import os
import json

# Caminho do arquivo para armazenar os dados dos usuários
USER_DATA_FILE = os.path.join(os.path.dirname(__file__), "users.txt")
TRANSACTIONS_FILE = os.path.join(os.path.dirname(__file__), "transactions.txt")

def load_transactions(user_id):
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            return [t for t in transactions if t.get("user_id") == user_id]  # Filtra pelo ID do usuário
    return []
    
def save_transactions(transaction):
    """
    Salva uma nova transação no arquivo.
    """
    transactions = load_transactions(transaction.get("user_id"))
    transactions.append(transaction)  # Adiciona a nova transação
    with open(TRANSACTIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)

# Função para carregar os usuários do arquivo
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# Função para salvar os usuários no arquivo
def save_users(users):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

# Carregar os usuários ao iniciar
users = load_users()

def register_user(user_id, name, email, password):
    """
    Registra um novo usuário com nome, email e senha.
    """
    if email in users:
        return False, "E-mail já registrado."
    users[user_id] = {
        'id': user_id,
        'name': name,
        'email': email,
        'password': password,
        'phone': None,  # Inicializa o telefone como None
    }
    save_users(users)  # Salvar os dados atualizados no arquivo
    return True, "Usuário registrado com sucesso."

def authenticate_user(email, password):
    """
    Autentica um usuário com email e senha.
    """
    for user in users.values():  # Itera sobre os valores do dicionário
        if user['email'] == email and user['password'] == password:
            return True, user  # Retorna o usuário autenticado
    return False, "Credenciais inválidas."

def get_user_by_id(user_id):
    """
    Retorna os dados do usuário pelo ID.
    """
    return users.get(user_id, None)  # Retorna None se o usuário não for encontrado

def get_user_credentials(user_id):
            """
            Retorna o nome, email e senha atuais do usuário.
            """
            user = get_user_by_id(user_id)
            if user:
                return user['name'], user['email'], user['password'], user['phone']
            return None, None, None

def update_user(user_id, name=None, email=None, password=None, phone=None):
    """
    Atualiza os dados do usuário.
    """
    if user_id not in users:
        return False, "Usuário não encontrado."
    if email and email != users[user_id]['email']:
        if email in [user['email'] for user in users.values()]:
            return False, "E-mail já registrado."
    if name:
        users[user_id]['name'] = name
    if email:
        users[user_id]['email'] = email
    if password:
        users[user_id]['password'] = password
    if phone:
        users[user_id]['phone'] = phone
    save_users(users)  # Salvar os dados atualizados no arquivo
    return True, "Usuário atualizado com sucesso."