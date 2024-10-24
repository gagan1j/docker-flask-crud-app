
from flask import Flask, render_template, request, jsonify  # Add render_template to imports
import sqlite3


app = Flask(__name__)
DATABASE = 'data.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')  
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    name = data['name']
    conn = get_db_connection()
    conn.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User created!"})

@app.route('/read', methods=['GET'])
def read():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(row) for row in users])

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    name = data['name']
    conn = get_db_connection()
    conn.execute('UPDATE users SET name = ? WHERE id = ?', (name, id))
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated!"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted!"})

if __name__ == '__main__':
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    conn.close()
    app.run(host='0.0.0.0', port=5000)
