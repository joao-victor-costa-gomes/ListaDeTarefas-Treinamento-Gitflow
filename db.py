import sqlite3

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

# Função para criar a tabela de tarefas
def create_table():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL)''')
    conn.commit()
    conn.close()