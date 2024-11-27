# Demande des valeurs à l'utilisateur
num1 = int(input("Entrez la valeur 1: "))
operator = input("Entrez l'opérateur (+, -, *, /, %): ")
num2 = int(input("Entrez la valeur 2 : "))

# Fonction calcul
def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur: division par zéro"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur: division par zéro"
    else:
        return "Opérateur invalide"

# Appel de la fonction avec les arguments fournis
resultat = calcule(num1, operator, num2)
print("Résultat :", resultat)
