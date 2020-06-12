#Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

n1=int(input("Ingrese un valor: "))
n2=int(input("Ingrese un valor: "))
n3=int(input("Ingrese un valor: "))

#print(n1, n2, n3)

if(n1>=n2 and n1>=n3):
    if(n2>n3):
        print(n1, n2, n3)
    else:
        print(n1,n3,n2)
elif(n2>=n1 and n2>=n3):
    if(n1>n3):
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)
elif(n3>=n2 and n3>=n1):
    if(n2>n1):
        print(n3,n2,n1)
    else:
        print(n3,n1,n2)
    
