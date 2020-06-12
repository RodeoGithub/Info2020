#Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. 
# Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.

inversion1=int(input("Inversion de la persona 1:"))
inversion2=int(input("Inversion de la persona 2:"))
inversion3=int(input("Inversion de la persona 3:"))

totalEmpresa=inversion1+inversion2+inversion3

print("A la persona 1 le corresponde el "+ str(round((inversion1*100)/totalEmpresa))+"%")
print("A la persona 2 le corresponde el "+ str(round((inversion2*100)/totalEmpresa))+"%")
print("A la persona 3 le corresponde el "+ str(round((inversion3*100)/totalEmpresa))+"%")

