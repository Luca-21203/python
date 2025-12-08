def nums_que_comencen_per(llista, lletra):
    comptador = 0
    for nom in llista:
        if nom.lower().startswith(lletra.lower()):
            comptador += 1
    return comptador


# Demanar la llista de noms a l'usuari
llista = []
print("Introdueix noms. Escriu 'fi' per acabar:")

while True:
    nom = input("Nom: ")

    if nom == "fi":
        break

    llista.append(nom)


# Demanar la lletra
lletra = input("Introdueix una lletra: ")


# Mostrar el resultat
print(nums_que_comencen_per(llista, lletra))
