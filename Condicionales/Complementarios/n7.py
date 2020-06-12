#Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. 
# Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, 
# si es que corresponde

compra= int(input("Ingrese el monto de la compra: "))

if(compra>1000):
    print("recibe un descuento del 15%!!")
    print("debe pagar: $"+str(compra-(compra*0.15)))
else:
    print("debe pagar:", compra )
