def calculadora():
    """
    Calculadora amb operacions bàsiques i canvis de base.
    """
    print("=== CALCULADORA ===")
    print("Operacions disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicació (*)")
    print("4. Divisió (/)")
    print("5. Canvi de base")
    print("0. Sortir")
    
    while True:
        opcio = input("\nTria una opció: ")
        
        if opcio == "0":
            print("Adéu!")
            break
        
        elif opcio in ["+", "1"]:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segon número: "))
            print(f"Resultat: {num1 + num2}")
        
        elif opcio in ["-", "2"]:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segon número: "))
            print(f"Resultat: {num1 - num2}")
        
        elif opcio in ["*", "3"]:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segon número: "))
            print(f"Resultat: {num1 * num2}")
        
        elif opcio in ["/", "4"]:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segon número: "))
            if num2 != 0:
                print(f"Resultat: {num1 / num2}")
            else:
                print("Error: No es pot dividir per zero!")
        
        elif opcio == "5":
            canvi_base()
        
        else:
            print("Opció no vàlida!")


def canvi_base():
    """
    Converteix un número entre diferents bases: binari, octal, decimal, hexadecimal.
    """
    print("\n=== CANVI DE BASE ===")
    print("Bases disponibles:")
    print("1. Binari (base 2)")
    print("2. Octal (base 8)")
    print("3. Decimal (base 10)")
    print("4. Hexadecimal (base 16)")
    
    base_origen = input("\nBase d'origen (1-4): ")
    numero = input("Introdueix el número: ")
    
    # Convertir el número a decimal primer
    try:
        if base_origen == "1":  # Binari
            decimal = int(numero, 2)
        elif base_origen == "2":  # Octal
            decimal = int(numero, 8)
        elif base_origen == "3":  # Decimal
            decimal = int(numero, 10)
        elif base_origen == "4":  # Hexadecimal
            decimal = int(numero, 16)
        else:
            print("Base d'origen no vàlida!")
            return
        
        # Mostrar el número en totes les bases
        print(f"\n--- Conversions de '{numero}' ---")
        print(f"Decimal:      {decimal}")
        print(f"Binari:       {bin(decimal)}")
        print(f"Octal:        {oct(decimal)}")
        print(f"Hexadecimal:  {hex(decimal)}")
        
    except ValueError:
        print("Error: Número no vàlid per a la base seleccionada!")


# Executar la calculadora
calculadora()
