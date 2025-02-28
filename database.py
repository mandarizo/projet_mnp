import sqlite3

# Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
def create_db():
    conn = sqlite3.connect('projets.db')
    c = conn.cursor()

    # Création de la table
    c.execute('''
        CREATE TABLE IF NOT EXISTS projets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            description TEXT,
            statut TEXT,
            date_debut TEXT,
            date_fin TEXT,
            responsable TEXT,
            budget REAL,
            obstacles TEXT
        )
    ''')

    # Sauvegarder et fermer la connexion
    conn.commit()
    conn.close()

# Appel de la fonction pour créer la base de données
if __name__ == '__main__':
    create_db()
