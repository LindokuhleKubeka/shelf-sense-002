from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('inventory.db')
    conn.execute('CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY, item TEXT, quantity INTEGER)')
    conn.commit()
    conn.close()

@app.route('/stock', methods=['POST'])
def add_stock():
    data = request.get_json()
    item = data['item']
    quantity = data['quantity']
    conn = sqlite3.connect('inventory.db')
    conn.execute('INSERT INTO stock (item, quantity) VALUES (?, ?)', (item, quantity))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Added {quantity} of {item} to inventory."})

@app.route('/stock', methods=['GET'])
def get_stock():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.execute('SELECT * FROM stock')
    stock = [{'id': row[0], 'item': row[1], 'quantity': row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify({"stock": stock})

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)