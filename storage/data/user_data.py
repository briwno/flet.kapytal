import os
import json

# Caminho do arquivo para armazenar os dados dos usuários
USER_DATA_FILE = os.path.join(os.path.dirname(__file__), "users.txt")

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

def register_user(name, email, password):
    """
    Registra um novo usuário com nome, email e senha.
    """
    if email in users:
        return False, "E-mail já registrado."
    users[email] = {
        'name': name,
        'email': email,
        'password': password
    }
    save_users(users)  # Salvar os dados atualizados no arquivo
    return True, "Usuário registrado com sucesso."

def authenticate_user(email, password):
    """
    Autentica um usuário com email e senha.
    """
    user = users.get(email)
    if user and user['password'] == password:
        return True, user['name']  # Retorna o nome do usuário em caso de sucesso
    return False, "Credenciais inválidas."
