import random
import string

def generate_password(length):
    if length < 4:
        print("La longueur du mot de passe doit être d'au moins 4 caractères.")
        return None

    # Ensemble de caractères
    lowercase = string.ascii_lowercase  # Lettres minuscules
    uppercase = string.ascii_uppercase  # Lettres majuscules
    digits = string.digits             # Chiffres
    special_chars = string.punctuation # Caractères spéciaux

    # Garantir qu'il y ait au moins un caractère de chaque type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Ajouter des caractères aléatoires pour compléter la longueur demandée
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Mélanger les caractères pour plus de sécurité
    random.shuffle(password)

    return ''.join(password)

# Demander à l'utilisateur la longueur du mot de passe
try:
    length = int(input("Entrez la longueur souhaitée pour le mot de passe : "))
    password = generate_password(length)
    if password:
        print("Votre mot de passe généré :", password)
except ValueError:
    print("Veuillez entrer un nombre valide.")
