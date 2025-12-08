def paraula_mes_llarga(llista):
    mes_llarga = llista[0]
    for paraula in llista:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga


# Demanar la llista de paraules a l'usuari
llista = []
print("Introdueix paraules. Escriu 'fi' per acabar:")

while True:
    paraula = input("Paraula: ")

    if paraula == "fi":
        break

    llista.append(paraula)


# Mostrar el resultat
if len(llista) > 0:
    print(paraula_mes_llarga(llista))
else:
    print("La llista està buida")
