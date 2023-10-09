# Input the month name
mois = input("Enter the name of the month: ")
# Determine the number of days in the month
if mois in ['Janvier', 'Mars', 'Mai', 'Juillet', 'Août', 'Octobre', 'Décembre']:
    jours = 31
elif mois in ['Avril', 'Juin', 'Septembre', 'Novembre']:
    jours = 30
elif mois == 'Février':
    jours = 28
else:
    jours = 0  # if the user enter an invalid month input

# the result
print("The month of", mois, "has", jours, "days.")
