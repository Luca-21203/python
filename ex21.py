def es_palindrom(paraula):
    invertida = ""
    for c in paraula:
        invertida = c + invertida
    return paraula == invertida


while True:
    text = input("Introdueix una paraula (o escriu 'sortir' per acabar): ")

    if text == "sortir":
        break

    print(es_palindrom(text))
