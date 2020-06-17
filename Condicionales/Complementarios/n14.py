#Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el 
# segundo que los reste y si no que los sume.

a = int(input("Ingrese un numero: "))

b = int(input("Ingrese un numero: "))

if(a==b):
    print(a*b)
elif(a>b):
    print(a-b)
else:
    print(a+b)
    