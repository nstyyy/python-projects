from db_connection import get_connection

def infos_client():
    client_id = input("Entrez l'id du client : ")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM clients WHERE id = %s"
        cursor.execute(query, (client_id,))
        result = cursor.fetchone()

        print("Nom : " + result[2])
        print("Prénom : " + result[1])
        print("Téléphone : " + result[3])
        print("Mail : " + result[4])
        print("Solde : " + result[5])
    except Exception as e:
        print("Erreur lors de la prise d'informations du client :", e)
    finally:
        connection.close()

def add_client():
    prenom = input("Entrez le prénom : ")
    nom = input("Entrez le nom : ")
    telephone = input("Entrez le numéro de téléphone : ")
    email = input("Entrez l'adresse e-mail : ")

    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO clients (prenom, nom, telephone, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (prenom, nom, telephone, email))
        connection.commit()
        print("Client ajouté avec succès !")
    except Exception as e:
        print("Erreur lors de l'ajout du client :", e)
    finally:
        connection.close()

def modify_client():
    client_id = input("Entrez l'ID du client à modifier : ")
    print("1. Modifier le prénom")
    print("2. Modifier le nom")
    print("3. Modifier l'email")
    choice = input("Choisissez une option : ")

    try:
        connection = get_connection()
        cursor = connection.cursor()

        if choice == "1":
            new_value = input("Entrez le nouveau prénom : ")
            query = "UPDATE clients SET prenom = %s WHERE id = %s"
        elif choice == "2":
            new_value = input("Entrez le nouveau nom : ")
            query = "UPDATE clients SET nom = %s WHERE id = %s"
        elif choice == "3":
            new_value = input("Entrez le nouvel email : ")
            query = "UPDATE clients SET email = %s WHERE id = %s"
        else:
            print("Option invalide.")
            return

        cursor.execute(query, (new_value, client_id))
        connection.commit()
        print("Client modifié avec succès !")
    except Exception as e:
        print("Erreur lors de la modification du client :", e)
    finally:
        connection.close()

def delete_client():
    client_id = input("Entrez l'ID du client à supprimer : ")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "DELETE FROM clients WHERE id = %s"
        cursor.execute(query, (client_id,))
        connection.commit()
        print("Client supprimé avec succès !")
    except Exception as e:
        print("Erreur lors de la suppression du client :", e)
    finally:
        connection.close()
