def sumar_llista(llista):
    suma = 0
    for x in llista:
        suma += x
    return suma


def multiplicar_llista(llista):
    producte = 1
    for x in llista:
        producte *= x
    return producte


llista = []

print("Introdueix números un per un. Escriu 'fi' per acabar.")

while True:
    valor = input("Número: ")

    if valor == "fi":
        break

    llista.append(float(valor))


opcio = input("Vols sumar o multiplicar? (s/m): ")

if opcio == "s":
    print("Resultat:", sumar_llista(llista))

elif opcio == "m":
    print("Resultat:", multiplicar_llista(llista))

else:
    print("Opció no vàlida")

