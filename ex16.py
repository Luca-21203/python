def gran_de_tres(num1, num2, num3):
    """
    Donats tres números, retorna el major.
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# Proves amb diferents exemples
print(gran_de_tres(5, 3, 8))       # 8
print(gran_de_tres(10, 20, 15))    # 20
print(gran_de_tres(7, 7, 7))       # 7
print(gran_de_tres(-5, -10, -3))   # -3
print(gran_de_tres(0, 100, 50))    # 100
print(gran_de_tres(3.5, 2.8, 4.1)) # 4.1
print(gran_de_tres(-15, 0, -20))   # 0
print(gran_de_tres(100, 99, 101))  # 101
