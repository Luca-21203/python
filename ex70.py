def divisio_segura(a, b):
    if b == 0:
        print("ERROR: No es pot dividir per zero")
        return None
    else:
        return a / b


# Demanar els dos números a l'usuari
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

# Cridar la funció
resultat = divisio_segura(num1, num2)

# Mostrar el resultat només si no és None
if resultat is not None:
    print("El resultat de la divisió és:", resultat)
