from db_connection import get_connection

def depot():
    client_id = input("Entrez l'ID du client pour le dépôt : ")
    montant = float(input("Entrez le montant à déposer : "))

    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "UPDATE clients SET solde = solde + %s WHERE id = %s"
        cursor.execute(query, (montant, client_id))
        connection.commit()
        print("Dépôt effectué avec succès !")
    except Exception as e:
        print("Erreur lors du dépôt :", e)
    finally:
        connection.close()

def retrait():
    client_id = input("Entrez l'ID du client pour le retrait : ")
    montant = float(input("Entrez le montant à retirer : "))

    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT solde FROM clients WHERE id = %s"
        cursor.execute(query, (client_id,))
        solde = cursor.fetchone()[0]

        if solde >= montant:
            update_query = "UPDATE clients SET solde = solde - %s WHERE id = %s"
            cursor.execute(update_query, (montant, client_id))
            connection.commit()
            print("Retrait effectué avec succès !")
        else:
            print("Fonds insuffisants.")
    except Exception as e:
        print("Erreur lors du retrait :", e)
    finally:
        connection.close()

def virement():
    source_id = input("Entrez l'ID du client source : ")
    dest_id = input("Entrez l'ID du client destinataire : ")
    montant = float(input("Entrez le montant à transférer : "))

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Vérifier le solde du client source
        query = "SELECT solde FROM clients WHERE id = %s"
        cursor.execute(query, (source_id,))
        solde_source = cursor.fetchone()[0]

        if solde_source >= montant:
            # Effectuer le transfert
            debit_query = "UPDATE clients SET solde = solde - %s WHERE id = %s"
            credit_query = "UPDATE clients SET solde = solde + %s WHERE id = %s"
            cursor.execute(debit_query, (montant, source_id))
            cursor.execute(credit_query, (montant, dest_id))
            connection.commit()
            print("Virement effectué avec succès !")
        else:
            print("Fonds insuffisants.")
    except Exception as e:
        print("Erreur lors du virement :", e)
    finally:
        connection.close()
