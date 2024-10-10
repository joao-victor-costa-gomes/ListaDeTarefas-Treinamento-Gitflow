from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection, create_table  # Importa as funções do db.py

app = Flask(__name__)

# Rota para exibir as tarefas
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_table()  # Chama a função para criar a tabela
    app.run(debug=True)

