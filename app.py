import os
from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect('projets.db')
    return conn

@app.route('/projets', methods=['GET'])
def get_projets():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM projets')
    projets = c.fetchall()
    conn.close()
    return jsonify(projets)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Utilise le port défini par Render
    app.run(host='0.0.0.0', port=port, debug=True)
