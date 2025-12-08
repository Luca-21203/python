def crear_punts(llista):
    for nombre in llista:
        print("." * int(nombre))


# Demanar la llista a l'usuari
llista = []
print("Introdueix números enters. Escriu 'fi' per acabar:")

while True:
    valor = input("Número: ")

    if valor == "fi":
        break

    llista.append(int(valor))


# Cridar la funció
crear_punts(llista)
