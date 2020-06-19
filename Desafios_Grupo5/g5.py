''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    Dado de los valores ingresados por el usuario (base, altura) 
    calcular y mostrar en pantalla el área de un triángulo.
'''
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la altura: "))

print("El area del triangulo es: ", (base*altura)/2)



'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    En una determinada empresa, sus empleados son evaluados al final 
    de cada año. Los puntos que pueden obtener en la evaluación comienzan 
    en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
    Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 
    o más, pero no valores intermedios entre las cifras mencionadas. 
    A continuación se muestra una tabla con los niveles correspondientes 
    a cada puntuación. La cantidad de dinero conseguida en cada nivel 
    es de 10000$ multiplicada por la puntuación del nivel.
        Nivel	        Puntuación
        Inaceptable	        0.0
        Aceptable	        0.5
        Meritorio	        0.6 o más
    Imprima por pantalla el nivel en que se encuentra el empleado, 
    la puntuación y la cantidad de dinero conseguida.
'''

puntaje = float(input("Ingrese la puntuacion obtenida: "))
if(puntaje >= 0.6):
    print(f"Meritorio!!\nObtuvo {10000*puntaje}")
elif(puntaje == 0.5):
    print(f"Aceptable!\nObtuvo {10000*puntaje}")
elif(puntaje == 0.0):
    print(f"Inaceptable..\nObtuvo {10000*puntaje}")


'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3: 
    Cree un programa que pida números hasta que se introduzca un cero. 
    Debe imprimir la suma total de todos los numeros introducidos y el promedio.
'''
n = int(input("Ingrese un numero: "))
sumaTotal = 0
count = 0
while ( n != 0):
    sumaTotal += n
    count+=1
    n = int(input("Ingrese un numero: "))
print(f"La suma total de todos los numeros introducidos es: {sumaTotal}\nEl promedio es: {round(sumaTotal/count,2)}")

'''
    -----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Crea una aplicación que permita adivinar un número. 
    La aplicación genera un número aleatorio del 1 al 100. 
    A continuación va pidiendo números y va respondiendo 
    si el número a adivinar es mayor o menor que el introducido,
    además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
    El programa termina cuando se acierta el número (además te dice en 
    cuantos intentos lo has acertado), si se llega al limite de intentos 
    te muestra el número que había generado.
'''

from random import randrange

magicNum = randrange(1,100)

encontro = False

intentosRestantes = 10

print("Intente adivinar el numero!")
intento = int(input("Ingrese el numero magico: "))

while( not encontro and intentosRestantes>0):
    intentosRestantes-=1
    if(intento == magicNum):
        print(f"Ha acertado!! en {10-intentosRestantes} intentos. Felicitaciones")
        encontro = True
    elif(intento>magicNum):
        print("El numero que ingreso es mayor al numero magico!\nIntente denuevo")
        print(f"Aun le quedan {intentosRestantes} intentos")
        intento = int(input("Ingrese el numero magico: "))
    else:
        print("El numero que ingreso es menor al numero magico!\nIntente denuevo")
        print(f"Aun le quedan {intentosRestantes} intentos")
        intento = int(input("Ingrese el numero magico: "))
if(not encontro):
    print(f"Alcanzo el limite de intentos permitidos...\nEl numero magico era{magicNum}")
