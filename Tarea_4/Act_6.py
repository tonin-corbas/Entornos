import math


A = int(input("Escribe un número: "))

if A <= 0:
    print("Ha ocurrido un error.")
else:
    cuad = A **2
    rzc = math.sqrt(A)
    print("El cuadrado de ",A, "es ",cuad)
    print("La raíz cuadrada de ",A, "es ",rzc)