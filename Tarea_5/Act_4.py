cont = 1
A = input("Escriba la contraseña: ")
if A == "Eureka":
    print("Contraseña correcta")
else:
    while cont < 3 and A != "Eureka" :
        A = input("Vuelva a introducir la contraseña: ")
        cont = cont + 1
    if cont == 3:
        print("Has utilizado todos los intentos, su cuenta será bloqueada temporalmente.")
    if A == "Eureka":
        print("Contraseña correcta")