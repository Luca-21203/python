def gran_llista(llista):
    major = llista[0]
    for x in llista:
        if x > major:
            major = x
    return major


# Demanar la llista a l'usuari
llista = []
print("Introdueix números enters. Escriu 'fi' per acabar:")

while True:
    valor = input("Número: ")

    if valor == "fi":
        break

    llista.append(int(valor))


# Mostrar el resultat
if len(llista) > 0:
    print(gran_llista(llista))
else:
    print("La llista està buida")
