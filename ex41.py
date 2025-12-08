# Demanar un número menor de 100
n = int(input("Introdueix un número menor de 100: "))

while n >= 100:
    n = int(input("Error. Introdueix un número menor de 100: "))

# Calcular la suma dels quadrats
suma = 0
num = n - 4   # El següent número per sota

while num >= 0:
    suma += num ** 2
    num -= 4

# Mostrar resultat
print("La suma dels quadrats és:", suma)
