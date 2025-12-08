# Demanar un número entre 1 i 900000
num = int(input("Introdueix un número entre 1 i 900000: "))

while num < 1 or num > 900000:
    num = int(input("ERROR. Introdueix un número entre 1 i 900000: "))

# Comptar els dígits
comptador = 0
aux = num

while aux > 0:
    aux //= 10
    comptador += 1

# Mostrar el resultat
print("El número té", comptador, "dígits")
