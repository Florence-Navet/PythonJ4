#definir la moyennes
def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

#demande à l'utilisateur de rentrer les notes
note1 = float(input("Entrez la première note: "))
note2 = float(input("Entrez la deuxième note: "))
note3 = float(input("Entrez la troisième note: "))

#Calculer la moyenne en appelant la fct
moyenne_etudiant = moyenne(note1, note2, note3)

#Afficher message en fct de la moyenne
if 15 <= moyenne_etudiant <= 20:
    print("Très bon élévè.")
elif 11 <= moyenne_etudiant <=14:
    print("Bon élève.")   
elif 8 <= moyenne_etudiant <= 10:
    print("Elève moyen.")
elif 0 <= moyenne_etudiant <= 7:
    print("Elève devant faire des efforts.")  
else:
    print("Note invalide.")    