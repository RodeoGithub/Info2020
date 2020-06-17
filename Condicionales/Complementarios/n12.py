#Hacer un programa que imprima el nombre de un artículo, clave, 
# precio original y su precio con descuento. El descuento lo hace en base a la clave, 
# si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en del 20%
# (solo existen dos claves).

nombre = input("Ingrese el nombre del articulo: ")

precio = float(input("Ingrese el precio del articulo: "))

clave = input("Ingrese la clave del producto: ")

if(clave == "01"):
    desc = 0.1
else:
    desc = 0.2

print("El precio con descuento es: ", precio-(precio*desc))



