
import sqlite3
from .logger import setup_logger

logger = setup_logger("SID_Database_v2")
DB_FILE = 'sid_users.db'

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row # Permite acessar colunas por nome
    return conn

def init_db():
    """Cria e atualiza a tabela de usuários com os campos de uso."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Adiciona a coluna 'usage_count' para rastrear o uso
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                plan TEXT DEFAULT 'free' NOT NULL,
                usage_count INTEGER DEFAULT 0 NOT NULL
            );
        ''')
        conn.commit()
        conn.close()
        logger.info("Banco de dados de usuários verificado/atualizado com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao inicializar o banco de dados: {e}")

# --- Funções Auxiliares para Gerenciar Usuários ---

def get_user_by_id(user_id):
    """Busca um usuário pelo seu ID."""
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    return user

def increment_user_usage(user_id):
    """Incrementa a contagem de uso de um usuário."""
    conn = get_db_connection()
    conn.execute('UPDATE users SET usage_count = usage_count + 1 WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

# Inicializa o banco de dados ao carregar o módulo
init_db()
