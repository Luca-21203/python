comptador = 0

for num in range(2, 101):
    es_primer = True

    for i in range(2, num):
        if num % i == 0:
            es_primer = False
            break

    if es_primer:
        print(num, end=" ")
        comptador += 1

print("\n\nTotal de nombres primers:", comptador)
