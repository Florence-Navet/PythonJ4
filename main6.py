# Entrez un nombre
nombre = int(input("Entrez un nombre: "))

# Fonction qui vérifie le signe du nombre
def verif_nombre(nombre):
    if nombre > 0:
        print("Ce nombre est positif.")
    elif nombre < 0:
        print("Ce nombre est négatif.") 
    else: 
        print("Ce nombre est nul.")    

# Appel de la fonction avec le nombre saisi
verif_nombre(nombre)
