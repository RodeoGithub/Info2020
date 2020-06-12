#Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario 
# para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma: 
# 0 – 6000							15% 
# 6000 – 7900					   10%
# 7900 – 12000					6%
# Más de 12000				   0%
#Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento,
# el sueldo actual y el sueldo aumentado.


salario=int(input("ingrese su salario: "))

if(salario>=0 and salario<=6000):
    print("su salario actual es:", salario)
    print("el aumento que le corresponde es: 15%" )
    print("su salario aumentado es:", salario+(salario*0.15))
elif(salario<=7900):
    print("su salario actual es:", salario)
    print("el aumento que le corresponde es: 10%" )
    print("su salario aumentado es:", salario+(salario*0.1))
elif(salario<=12000):
    print("su salario actual es:", salario)
    print("el aumento que le corresponde es: 6%" )
    print("su salario aumentado es:", salario+(salario*0.06))
else:
    print("su salario actual es:", salario)
    print("el aumento que le corresponde es: 0%" )
    print("su salario aumentado es:", salario)

