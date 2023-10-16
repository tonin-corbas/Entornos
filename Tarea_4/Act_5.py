
num1 = float(input("Escribe un número: "))
num2 = float(input("Escribe otro número: "))
num3 = float(input("Escribe un último número: "))

if num1 < 0:
    resultado = num1 * num2 * num3
    print("El producto de los tres números es:", resultado)
else:
    resultado = num1 + num2 + num3
    print("La suma de los tres números es:", resultado)
