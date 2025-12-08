def comptar_vocals(paraula):
    paraula = paraula.lower()
    a = e = i = o = u = 0

    for lletra in paraula:
        if lletra == "a":
            a += 1
        elif lletra == "e":
            e += 1
        elif lletra == "i":
            i += 1
        elif lletra == "o":
            o += 1
        elif lletra == "u":
            u += 1

    print("Hi ha", a, "a's,", e, "e's,", i, "i's,", o, "o's i", u, "u's")


# Demanar una paraula a l'usuari
paraula = input("Introdueix una paraula: ")

# Cridar la funció
comptar_vocals(paraula)
