# Demanar un número a l'usuari
num = input("Introdueix un número: ")

print("Dígits parells del número:")

for digit in num:
    if int(digit) % 2 == 0:
        print(digit)
