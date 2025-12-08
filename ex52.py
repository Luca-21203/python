def crear_llista_fitxer(nom_fitxer):
    llista = []
    fitxer = open(nom_fitxer, "r")

    for linia in fitxer:
        paraules = linia.split()
        for paraula in paraules:
            llista.append(paraula)

    fitxer.close()
    return llista


# Demanar el nom del fitxer a l'usuari
nom_fitxer = input("Introdueix el nom del fitxer: ")

# Cridar la funció
llista = crear_llista_fitxer(nom_fitxer)

# Mostrar el resultat
print(llista)
