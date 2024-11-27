# fct time_to_text
def time_to_text(minutes):
    heures = minutes // 60
    reste_minutes = minutes % 60
    print(f"{heures} heures et {reste_minutes} minutes")


# Faire entrer à l'utilisateur un nombre entier de minutes
minutes = int(input("Entrez un nombre de minutes: "))

# appel de la fonction avec l'argument 'minutes'
time_to_text(minutes)
