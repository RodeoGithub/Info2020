#Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) 
# de acuerdo al tamaño indicado. Por ejemplo el gráfico a la izquierda es el resultado 
# de un tamaño: 8x6

x = int(input("Ingrese la cantidad de filas: "))
y = int(input("Ingrese la cantidad de columnas: "))

f = True
blanco = '\33[7m'
verde = '\33[42m'
final = '\33[0m'
for i in range(0,x):
    for j in range(0,y):
        if (f):
            if(j%2==0):
                print(f"{blanco}  {final}", end="")
            else:
                print(f"{verde}  {final}", end="")
        else:
            if(j%2==0):
                print(f"{verde}  {final}", end="")
            else:
                print(f"{blanco}  {final}", end="")
    f = not f
    print()
