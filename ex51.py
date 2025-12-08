def elimina_duplicats(llista):
    nova_llista = []
    for element in llista:
        if element not in nova_llista:
            nova_llista.append(element)
    return nova_llista


# Demanar la llista a l'usuari
llista = []
print("Introdueix elements. Escriu 'fi' per acabar:")

while True:
    valor = input("Element: ")
    
    if valor == "fi":
        break
    
    llista.append(valor)

# Mostrar el resultat
print(elimina_duplicats(llista))
