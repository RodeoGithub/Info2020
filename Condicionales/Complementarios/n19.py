#Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones 
# por cantidad según el siguiente criterio:

#i. a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.

#ii.a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, 
# el 5% y más de 18 unidades, el 10%.

#El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. 
# Dado el importe bruto de una compra de libros, el tipo de cliente de que se trata y la 
# cantidad total pedida por el mismo, determinar el importe bruto bonificado.

importe = float(input("ingrese el importe bruto de la compra: "))

tipoCliente = input("Ingrese le tipo de cliente (L para libreria / P para particular): ")

cantComprada = int(input("Ingrese la cantidad comprada: "))

if(tipoCliente.lower()=="l"):
    if(cantComprada>24):
        print(importe-(importe*0.25))
    else:
        print(importe-(importe*0.10))
else:
    if(cantComprada>18):
        print(importe-(importe*0.10))
    elif(cantComprada>6):
        print(importe-(importe*0.6))
    else:
        print(importe)

        