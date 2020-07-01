'''
Ejercicio 1:
Escribir un programa que pregunte por una muestra de números, 
separados por comas, los guarde en una lista y muestre por pantalla 
su promedio y desviación estándar.
'''

lista = input()
print(lista)


lista2 = list(lista.split(","))

suma=0

lista2 = [int(i) for i in lista2]
for num in lista2:
    suma+=int(num)
print(f"El promedio es: {suma/len(lista2)}")





'''
Ejercicio 2:
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, elimine los elementos repetidos (dejando únicamente el primero de los 
elementos repetidos).

'''

# Coloque la resolución del Ejercicio debajo de esta línea
c = int(input("Cuantas palabras quiere ingresar? :"))
lista = []
for i in range(c):
    p = input("Ingrese palabra: ")
    lista.append(p)
lista.reverse()
for i in lista:
    for j in range(lista.count(i)-1):
        lista.remove(i)
lista.reverse()
print(lista)


