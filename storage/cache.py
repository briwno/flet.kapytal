from storage.data.user_data import get_user_by_id, load_transactions

class DataCache:
    """
    Uma classe de cache simples para armazenar dados do usuário e transações
    para evitar chamadas de banco de dados repetidas e lentas.
    """
    def __init__(self):
        self.user_data = {}
        self.transactions = {}

    def get_user(self, user_id, force_refresh=False):
        """Busca os dados do usuário, utilizando o cache se disponível."""
        if user_id not in self.user_data or force_refresh:
            print(f"Cache miss for user {user_id}. Fetching from DB.")
            self.user_data[user_id] = get_user_by_id(user_id)
        else:
            print(f"Cache hit for user {user_id}.")
        return self.user_data.get(user_id)

    def get_transactions(self, user_id, force_refresh=False):
        """Busca as transações do usuário, utilizando o cache se disponível."""
        if user_id not in self.transactions or force_refresh:
            print(f"Cache miss for transactions of user {user_id}. Fetching from DB.")
            self.transactions[user_id] = load_transactions(user_id)
        else:
            print(f"Cache hit for transactions of user {user_id}.")
        return self.transactions.get(user_id)

    def clear_cache(self, user_id=None):
        """Limpa o cache, seja para um usuário específico ou para todos."""
        if user_id:
            self.user_data.pop(user_id, None)
            self.transactions.pop(user_id, None)
            print(f"Cache cleared for user {user_id}.")
        else:
            self.user_data.clear()
            self.transactions.clear()
            print("All cache cleared.")

# Instância única do cache para ser usada em todo o aplicativo
app_cache = DataCache()