#Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si 
# su promedio de tres calificaciones es mayor o igual a 70; 
# desaprueba en caso contrario.

n1 = int(input("ingrese una nota: "))
n2 = int(input("ingrese una nota: "))
n3 = int(input("ingrese una nota: "))

if(((n1+n2+n3)/3)>70):
    print("Aprueba")
else:
    print("Desaprueba")
