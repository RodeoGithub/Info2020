#Nos han pedido desarrollar una aplicación móvil para reducir comportamientos 
# inadecuados para el ambiente.
# a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa 
#   debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya 
#   ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de 
#   intentos. 
import getpass

correctUser = "admin"
correctPassword = "rodrigo"

print("Log in")
f = False
for i in range (1,4):
    user=input("Ingrese su usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")
    if(user==correctUser and password==correctPassword):
        print("Ingreso correcto! Bienvenido")
        f=True
        break
    print("Ingreso incorrecto! intente otra vez")
    if(3-i != 0):
        print("Intentos restantes:", (3-i))
if(not f):
    print("Ingreso bloqueado, intente mas tarde")

