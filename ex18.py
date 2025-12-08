def es_vocal(c):
    vocals = "aeiouAEIOU"
    
    # Comprovar que només sigui UN caràcter
    if len(c) != 1:
        return False
    
    return c in vocals


while True:
    caracter = input("Introdueix un caràcter (o escriu 'sortir' per acabar): ")

    if caracter == "sortir":
        break

    print(es_vocal(caracter))
