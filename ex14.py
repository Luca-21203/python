def menu_principal():
    opcio=0
    while opcio<1 or opcio>4:
        opcio = int(input(""" Elegeixi una opció:
                        1. Calculadora decimal
                        2. Calculadora real (floats)
                        3. Sortir
                        4. Conversió entre bases \n"""))
        if 1 <= opcio <= 4:
            return opcio
        else:
            print("L'opció seleccionada no és correcta. Torni-ho a provar!\n")


def menu_calculadora():
    opcio = -1
    while opcio < 0 or opcio > 4:
        opcio = int(input("""Elegeix una opció:
                1. Suma
                2. Resta
                3. Multiplicació
                4. Divisió
                0. Sortir
                """))
    return opcio


def calculadora_decimal(opcio):
    if 1 <= opcio <= 4:
        a = int(input("Introdueixi el primer número: "))
        b = int(input("Introdueixi el segon número: "))

    match opcio:
        case 1:
            print("Estic fent la suma!\n")
            print(f"El resultat de suma {a} + {b} és {a+b}")
        case 2:
            print("Estic fent la resta!\n")
            print(f"El resultat de restar {a} - {b} és {a-b}")
        case 3:
            print("Estic fent la multiplicació!\n")
            print(f"El resultat de multiplicar {a} * {b} és {a*b}")
        case 4:
            print("Estic fent la divisió!\n")
            print(f"El resultat de dividir {a} / {b} és {a//b}")
        case _:
            print("Sortint...\n")


def calculadora_real(opcio):
    if 1 <= opcio <= 4:
        a = float(input("Introdueixi el primer número: "))
        b = float(input("Introdueixi el segon número: "))

    match opcio:
        case 1:
            print("Estic fent la suma!\n")
            print(f"El resultat de suma {a} + {b} és {a+b}")
        case 2:
            print("Estic fent la resta!\n")
            print(f"El resultat de restar {a} - {b} és {a-b}")
        case 3:
            print("Estic fent la multiplicació!\n")
            print(f"El resultat de multiplicar {a} * {b} és {a*b}")
        case 4:
            print("Estic fent la divisió!\n")
            print(f"El resultat de dividir {a} / {b} és {a/b}")
        case _:
            print("Sortint...\n")



#      NOVA FUNCIÓ

def menu_conversions():
    op = -1
    while op < 0 or op > 8:
        op = int(input("""
        Conversió de bases – Elegeixi una opció:

        1. Decimal → Binari
        2. Decimal → Octal
        3. Decimal → Hexadecimal
        4. Binari → Decimal
        5. Octal → Decimal
        6. Hexadecimal → Decimal
        7. Binari → Hexadecimal
        8. Hexadecimal → Binari
        0. Sortir

        Opció: """))
    return op


def conversions_base():
    op = menu_conversions()

    match op:
        case 1:
            n = int(input("Introdueixi un número decimal: "))
            print(f"Binari: {bin(n)[2:]}")
        case 2:
            n = int(input("Introdueixi un número decimal: "))
            print(f"Octal: {oct(n)[2:]}")
        case 3:
            n = int(input("Introdueixi un número decimal: "))
            print(f"Hexadecimal: {hex(n)[2:].upper()}")
        case 4:
            n = input("Introdueixi un número binari: ")
            print(f"Decimal: {int(n, 2)}")
        case 5:
            n = input("Introdueixi un número octal: ")
            print(f"Decimal: {int(n, 8)}")
        case 6:
            n = input("Introdueixi un número hexadecimal: ")
            print(f"Decimal: {int(n, 16)}")
        case 7:
            n = input("Introdueixi un número binari: ")
            dec = int(n, 2)
            print(f"Hexadecimal: {hex(dec)[2:].upper()}")
        case 8:
            n = input("Introdueixi un número hexadecimal: ")
            dec = int(n, 16)
            print(f"Binari: {bin(dec)[2:]}")
        case 0:
            print("Tornant al menú principal...\n")



#      PROGRAMA PRINCIPAL


op = 1
while op != 0:
    op = menu_principal()

    if op == 1:
        print("Estic passant per la calculadora decimal!\n")
        calculadora_decimal(menu_calculadora())

    elif op == 2:
        print("Estic passant per la calculadora real!\n")
        calculadora_real(menu_calculadora())

    elif op == 4:
        print("Estic passant per les conversions de base!\n")
        conversions_base()

    else:
        print("Gràcies per utilitzar la meva calculadora. Fins un altre dia!\n")
        op = 0
