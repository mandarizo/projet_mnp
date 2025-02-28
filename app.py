from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

# Configuration de l'application Flask
app = Flask(__name__)
CORS(app)  # Permet d'éviter les problèmes de CORS entre ton frontend React et ton backend Flask

# Fonction pour se connecter à la base de données SQLite
def get_db():
    conn = sqlite3.connect('projets.db')
    return conn

# Route pour obtenir tous les projets
@app.route('/projets', methods=['GET'])
def get_projets():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM projets')
    projets = c.fetchall()
    conn.close()
    return jsonify(projets)

# Route pour ajouter un projet
@app.route('/projets', methods=['POST'])
def add_projet():
    data = request.get_json()
    nom = data['nom']
    description = data['description']
    statut = data['statut']
    date_debut = data['date_debut']
    date_fin = data['date_fin']
    responsable = data['responsable']
    budget = data['budget']
    obstacles = data['obstacles']

    conn = get_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO projets (nom, description, statut, date_debut, date_fin, responsable, budget, obstacles)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nom, description, statut, date_debut, date_fin, responsable, budget, obstacles))
    conn.commit()
    conn.close()

    return jsonify({"message": "Projet ajouté!"}), 201

# Démarrer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
