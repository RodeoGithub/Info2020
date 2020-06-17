#Se leen tres números que son las longitudes de los lados de un triángulo. 
# Determinar e informar si el mismo es equilátero (3 lados iguales), isósceles 
# (2 lados iguales) o escaleno (3 lados distintos).

l1 = int(input("Ingrese un lado: "))

l2 = int(input("Ingrese un lado: "))

l3 = int(input("Ingrese un lado: "))

if(l1 == l2 and l2 == l3):
    print("Es un triangulo equilatero")
elif(l1 != l2 and l2 != l3 and l1 != l3):
    print("Es un triangulo escaleno")
else:
    print("Es un triangulo isoceles")
    