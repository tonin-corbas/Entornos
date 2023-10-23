import math

A = int(input("Escribe un número: "))
suma = 0
cont = 1
while (A != -1):
    print("Escribe el siguiente el numero",)
    A = int(input(""))
    suma = suma + A
    cont = cont + 1

print("El promedio es ", suma/(cont-1))
