# Demanar el capital inicial
capital = float(input("Introdueix el capital inicial (50000€ - 800000€): "))

while capital < 50000 or capital > 800000:
    capital = float(input("ERROR. Introdueix un capital entre 50000€ i 800000€: "))

# Demanar l'interès
interes = float(input("Introdueix l'interès (0.5% - 13%): "))

while interes < 0.5 or interes > 13:
    interes = float(input("ERROR. Introdueix un interès entre 0.5% i 13%: "))

# Demanar els anys
anys = int(input("Introdueix el nombre d'anys (3 - 40): "))

while anys < 3 or anys > 40:
    anys = int(input("ERROR. Introdueix un nombre d'anys entre 3 i 40: "))

# Càlcul del capital final
capital_final = capital * (1 + interes / 100) ** anys

# Mostrar el resultat
print("El capital final serà de:", round(capital_final, 2), "€")
