def es_de_traspas(any):
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False


# Demanar l'any a l'usuari
any = int(input("Introdueix un any: "))

# Mostrar el resultat
print(es_de_traspas(any))
