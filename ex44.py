# Demanar un número entre 1 i 20
num = int(input("Introdueix un número entre 1 i 20: "))

while num < 1 or num > 20:
    num = int(input("ERROR. Introdueix un número entre 1 i 20: "))

# Imprimir la taula de multiplicar
print("Taula de multiplicar del", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
