import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Votre utilisateur MySQL
            password="",  # Votre mot de passe MySQL
            database="bank_system"
        )
        return connection
    except mysql.connector.Error as e:
        print("Erreur lors de la connexion à la base de données :", e)
        exit()
