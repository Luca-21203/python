def mostrar_majors_que(tupla, numero):
    for x in tupla:
        if x > numero:
            print(x)


# Demanar els valors de la tupla
valors = []
print("Introdueix números enters per a la tupla. Escriu 'fi' per acabar:")

while True:
    valor = input("Valor: ")

    if valor == "fi":
        break

    valors.append(int(valor))

tupla = tuple(valors)

# Mostrar els majors de 18
print("\nNúmeros majors de 18:")
mostrar_majors_que(tupla, 18)
