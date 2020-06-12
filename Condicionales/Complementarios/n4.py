#Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.


m=int(input("ingrese m: "))
n=int(input("ingrese n: "))

if(m%n==0):
    print("n es divisor de m")
else:
    print("n no es divisor de m")