# Demanar la potència a l'usuari
potencia = int(input("Introdueix la potència: "))

# Crear la llista amb list comprehension (del 0 al 9)
llista_potencies = [i ** potencia for i in range(10)]

# Mostrar el resultat
print(llista_potencies)
