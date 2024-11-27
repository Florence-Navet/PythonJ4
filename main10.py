#fonction genre nombre
def pair_impair (nombre):
    if isinstance(nombre, int)and nombre >= 0:
        if nombre % 2 == 0:
            print("Ce nombre est pair !!")
        else :
            print("ce nombre est impair.")   
    else:
        print("Veuillez entrer un nombre entier positif")  

#Appel de la fonction
pair_impair(4)   # Nombre pair
pair_impair(7)   # Nombre impair
pair_impair(10)  # Nombre pair
pair_impair(-3)  # Entrée invalide (négatif)
pair_impair(3.5) # Entrée invalide (non entier)
