#Un obrero necesita calcular su salario semanal, el cual se obtiene de la 
# siguiente manera:
# Si trabaja 40 horas o menos se le paga $16 por hora
# Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y 
# $20 por cada hora extra.

horasTrabajadas = int(input("Ingrese las horas trabajadas en la semana"))

if(horasTrabajadas<=40):
    print("Cobrara: " + "$" + str(horasTrabajadas*16))
else:
    print("Cobrara: " + "$" + str((40*16)+((horasTrabajadas-40)*20)))


