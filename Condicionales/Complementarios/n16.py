#Hacer un programa que calcule el total a pagar por la compra de camisas. 
# Si se compran tres camisas o mas se aplica un descuento del 20% sobre el total de la 
# compra y si son menos de tres camisas un descuento del 10%.

cCamisas = int(input("Ingrese la cantidad de camisas que va a comprar: "))

totalCompra = float(input("Ingrese el total de la compra: "))

if(cCamisas>=3):
    print(f"Total a pagar: $" + {totalCompra+(totalCompra*0.20)})
else:
    print(f"Total a pagar: $" + {totalCompra+(totalCompra*0.10)})
