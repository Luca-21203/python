def longitud(x):
    comptador = 0
    for _ in x:
        comptador += 1
    return comptador


# Demanar si vol una llista o una cadena
opcio = input("Vols introduir una llista o una cadena? (l/c): ")

if opcio == "c":
    text = input("Introdueix una cadena: ")
    print(longitud(text))

elif opcio == "l":
    llista = []
    print("Introdueix els valors de la llista. Escriu 'fi' per acabar.")

    while True:
        valor = input("Valor: ")
        if valor == "fi":
            break
        llista.append(valor)

    print(longitud(llista))

else:
    print("Opció no vàlida")
