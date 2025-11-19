def gran(num1, num2):
    """
    Donats dos números, retorna el major.
    """
    if num1 > num2:
        return num1
    else:
        return num2


# Proves amb diferents exemples
print(gran(5, 3))      # 5
print(gran(10, 20))    # 20
print(gran(-5, -10))   # -5
print(gran(7, 7))      # 7
print(gran(0, 100))    # 100
print(gran(3.5, 2.8))  # 3.5
print(gran(-15, 0))    # 0
