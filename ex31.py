# Demanar l'any actual
any_actual = int(input("Introdueix l'any actual: "))

noms = []
anys_naixement = []
edats = []

# Demanar dades de 4 persones
for i in range(3):
    print("\nPersona", i + 1)
    nom = input("Nom: ")
    any_naixement = int(input("Any de naixement: "))

    edat = any_actual - any_naixement

    noms.append(nom)
    anys_naixement.append(any_naixement)
    edats.append(edat)

# Mostrar dades tabulades
print("\nNom\t\tAny naixement\tAnys que farà aquest any")

for i in range(3):
    print(noms[i], "\t\t", anys_naixement[i], "\t\t", edats[i])
