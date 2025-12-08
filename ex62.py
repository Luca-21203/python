from functools import reduce

def Passar_a_Numero(llista):
    return reduce(lambda x, y: x * 10 + y, llista)


# Demanar la llista de dígits a l'usuari
llista = []
print("Introdueix dígits (0-9). Escriu 'fi' per acabar:")

while True:
    valor = input("Dígit: ")

    if valor == "fi":
        break

    llista.append(int(valor))


# Mostrar el resultat
print(Passar_a_Numero(llista))
