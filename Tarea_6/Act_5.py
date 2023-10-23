import math

A = int(input("Escribe una secuencia de números: "))
suma = 0
cont = 1
menor= A
mayor = A
while(A != 0):
    print("Escribe el siguiente el numero",)
    A = int(input(""))
    suma = suma + A
    cont = cont + 1
    if A < menor:
        menor = A
    if A > mayor:
        mayor = A
    promedio = suma/(cont -1)

print("El promedio es ",promedio)
print("El mayor es ",mayor)
print("El menor es ",menor)