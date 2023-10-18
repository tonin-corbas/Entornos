cont = 1
A = ""
while cont <= 10 and A != "Eureka" :
    A = input("Introduce la contraseña: ")
    cont = cont + 1
if cont > 10:
    print("Has utilizado todos los intentos, su cuenta será bloqueada temporalmente.")
if A == "Eureka":
    print("Contraseña correcta")