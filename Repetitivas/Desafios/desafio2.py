#Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.
# Realizá un programa que permita registrar cantidad de colillas recolectadas por un 
# número determinado de personas. Luego obtener estadísticas al respecto informando 
# porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos 
# de 200, más de 200 colillas.

cantPersonas = int(input("Ingrese la cantidad de personas: "))

menosDe100 = 0
menosDe200 = 0
masDe200 = 0

for i in range(0,cantPersonas):
    colillas = int(input("Cuantas colillas recolecto? "))
    if(colillas<100):
        menosDe100+=1
    elif(colillas<200):
        menosDe200+=1
    else:
        masDe200+=1

print("El porcentaje de personas que recolecto menos de 100 colillas es:", end=" ")
print(str(round((menosDe100*100)/cantPersonas)) + "%")

print("El porcentaje de personas que recolecto menos de 200 colillas es:", end=" ")
print(str(round((menosDe200*100)/cantPersonas)) + "%")

print("El porcentaje de personas que recolecto mas de 200 colillas es:", end=" ")
print(str(round((masDe200*100)/cantPersonas)) + "%" )

