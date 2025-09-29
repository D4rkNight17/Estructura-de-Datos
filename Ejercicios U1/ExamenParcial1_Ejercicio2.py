def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingresa un número entero positivo: "))

if num >= 0:
    binario = decimal_a_binario(num)
    print(f"El equivalente en binario de {num} es: {binario}")
else:
    print("Por favor ingresa un número entero positivo.")