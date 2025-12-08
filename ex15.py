def gran(a, b):
    if a > b:
        return a
    else:
        return b


# Demanar els dos números a l'usuari
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

# Mostrar el resultat
print(gran(num1, num2))
