# Demanar un número a l'usuari
num = input("Introdueix un número: ")

# Sumar els dígits
suma = 0
for digit in num:
    suma += int(digit)

# Mostrar la suma
print("La suma dels dígits és:", suma)

# Comprovar si és parell o senar
if suma % 2 == 0:
    print("La suma és parell")
else:
    print("La suma és senar")
