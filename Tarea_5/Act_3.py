A = int(input("Introduce un dia: "))
B = int(input("Introduce un mes: "))

if 1<= A <= 31:
    print("Día introducido correcto.")
else:
    print("Día introducido incorrecto")
if 1<= B <= 12:
    print("Més introducido correcto")
    print("la fecha es ",A, "/",B," del XXXX")
else:
    print("Més introducido incorrecto")
    
    