#Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, 
# de acuerdo a los siguientes casos. Suponiendo que A determina el mayor de los tres lados y B y C corresponden
# con los otros dos, entonces:
    #Si A>=B + C à No se trata de un triángulo
    #Si A2 = B2 + C2 à Es un triángulo rectángulo
    #Si A2 > B2 + C2 à Es un triángulo obtusángulo
    #Si A2 < B2 + C2 à Es un triángulo acutángulo

L1=int(input("ingrese un lado: "))
L2=int(input("ingrese un lado: "))
L3=int(input("ingrese un lado: "))

ladosAlCuadrado=(L2**2) + (L3**2)

if(L1>= (L2+L3)):
    print("No es un triangulo")
elif(L1**2 == ladosAlCuadrado):
	print("Es triangulo rectangulo")
elif(L1**2 > ladosAlCuadrado):
	print("Es triangulo obtusangulo")
elif(L1**2 < ladosAlCuadrado):
	print("Es triangulo acutangulo")