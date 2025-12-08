import os

# Ruta del directori
ruta = "/home/cicles/AO/Prova"

# Crear el directori si no existeix
os.makedirs(ruta, exist_ok=True)

# Canviar al directori
os.chdir(ruta)

# Crear el fitxer i escriure els companys
companys = [
    "IKER ANDRES ENSEÑAT",
    "YOUSSEF AZANAI",
    "RAUL BARROSO PONS",
    "OSAMA EL HAJOUI EL HAJOUI",
    "MOHAMED EL MAKADMI LAMKADEM",
    "POL FORNES CABRERA",
    "JOAN GÓMEZ CARRERAS",
    "IZAN GÓMEZ FERRO",
    "IKER HEREDIA HEREDIA",
    "AITOR HOLGADO HARTO",
    "MOHAMED MAMOUNI KASMI",
    "DANIEL MANTECA GARRIGA",
    "JUSTIN AARON MONTIEL CANCHINGRE",
    "RAFEL PASCUAL PONS",
    "EDGAR PELEGRÍ HITA",
    "IZAN PONS PONS",
    "CIRO FABIAN SALAS CARBALLO",
    "LUCAS SANTANA PREVI",
    "ARITZ SEGUÍ TALTAVULL",
    "RAUL SINTES RUIZ",
    "IAN SINTES SEGUI",
    "RUSSELL MIJAEL VÁSQUEZ CHURA"
]

with open("Ex12.txt", "w") as fitxer:
    for nom in companys:
        fitxer.write(nom + "\n")

# Obrir el fitxer per afegir els professors
professors = [
    "Joan Carreras Vinent",
    "Pep Malle",
    "JESÚS CAPÓ PONS",
    "IRENE COLL SERRA",
    "MANEL BOSCH MONJO",
    "David Labiano Boutens",
    "BELEN CABRERA LORENZO"
]

with open("Ex12.txt", "a") as fitxer:
    for nom in professors:
        fitxer.write(nom + "\n")

# Obrir el fitxer final i posar-ho dins una llista
with open("Ex12.txt", "r") as fitxer:
    llista_noms = fitxer.read().splitlines()

# Mostrar la llista final
print(llista_noms)
