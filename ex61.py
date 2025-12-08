def lenp(frase):
    paraules = frase.split()
    longituds = list(map(len, paraules))
    return longituds


# Demanar una frase a l'usuari
frase = input("Introdueix una frase: ")

# Mostrar el resultat
print(lenp(frase))
