# Demande à l'utilisateur d'entrer les valeurs
saison = input("Entrez une saison: printemps, été, automne ou hiver : ")
type_aliment = input("Entrez fruits ou légumes : ")

# Définition de la fonction
def aff_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été":
        print("artichaut, aubergine, navet")  
    else:
        print("Données introuvables.")   

# Appel de la fonction en passant les paramètres saisis par l'utilisateur
aff_aliments(type_aliment, saison)
