from client_manager import infos_client, add_client, modify_client, delete_client
from bank_actions import depot, retrait, virement

def main():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Gestion des clients")
        print("2. Actions bancaires")
        print("3. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            print("\n=== Gestion des clients ===")
            print("1. Voir les informations d'un client")
            print("2. Ajouter un client")
            print("3. Modifier un client")
            print("4. Supprimer un client")
            print("5. Retour au menu principal")
            client_choix = input("Choisissez une option : ")

            if client_choix == "1":
                infos_client()
            elif client_choix == "2":
                add_client()
            elif client_choix == "3":
                modify_client()
            elif client_choix == "4":
                delete_client()
            elif client_choix == "5":
                continue
            else:
                print("Option invalide.")

        elif choix == "2":
            print("\n=== Actions bancaires ===")
            print("1. Faire un dépôt")
            print("2. Faire un retrait")
            print("3. Faire un virement")
            print("4. Retour au menu principal")
            bank_choix = input("Choisissez une option : ")

            if bank_choix == "1":
                depot()
            elif bank_choix == "2":
                retrait()
            elif bank_choix == "3":
                virement()
            elif bank_choix == "4":
                continue
            else:
                print("Option invalide.")

        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
