# Demanar els dos números a l'usuari
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

# Assegurar que num1 sigui el menor
if num1 > num2:
    num1, num2 = num2, num1

# Calcular la suma
suma = 0
for i in range(num1, num2 + 1):
    suma += i

# Mostrar el resultat
print("La suma és:", suma)
