def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r") as fitxer:
            contingut = fitxer.read()
            return contingut
    except FileNotFoundError:
        print("ERROR: El fitxer no existeix.")
        return None
    except PermissionError:
        print("ERROR: No tens permís per obrir aquest fitxer.")
        return None
    except:
        print("ERROR: Hi ha hagut un problema en obrir o llegir el fitxer.")
        return None


# Demanar el nom del fitxer a l'usuari
nom = input("Introdueix el nom del fitxer: ")

# Llegir el fitxer utilitzant la funció
contingut = llegir_fitxer(nom)

# Mostrar el contingut només si s'ha pogut llegir
if contingut is not None:
    print("\nContingut del fitxer:")
    print(contingut)
