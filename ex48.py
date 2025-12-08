def esta_ordenada(llista):
    ascendent = True
    descendent = True

    for i in range(len(llista) - 1):
        if llista[i] > llista[i + 1]:
            ascendent = False
        if llista[i] < llista[i + 1]:
            descendent = False

    if ascendent:
        return "Està ordenada de forma ascendent"
    elif descendent:
        return "Està ordenada de forma descendent"
    else:
        return "No està ordenada"


# Demanar la llista a l'usuari
llista = []
print("Introdueix números enters. Escriu 'fi' per acabar:")

while True:
    valor = input("Número: ")

    if valor == "fi":
        break

    llista.append(int(valor))


# Mostrar el resultat
if len(llista) > 1:
    print(esta_ordenada(llista))
else:
    print("La llista ha de tenir almenys dos números")
