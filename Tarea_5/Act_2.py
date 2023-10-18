import math


A = int(input("Introduce un valor numérico: "))
B = int(input("Introduce otro valor numérico: "))

if A > B:
    Division = A/B
    print("La división entre ",A, "y ",B," da ",Division)
else:
    Division2 = B/A
    print("La división entre ",B, "y ",A," da ",Division2)