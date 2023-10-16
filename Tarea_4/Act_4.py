A = input("Escriba un número: ")
B = input("Escriba otro número: ")
C = input("Escriba un último número: ")

myr = 0 

if A > B and A > C: 
    myr = A
else:
    if B > C:
        myr = B
    else:
        myr = C

print("El mayor número es ",myr)