#En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. 
#El presupuesto anual del hospital se reparte conforme a la sig. tabla:
# Pediatría					60%
# Traumatología		 20%
# Kinesiología			 20%
#Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal que se ingrese por teclado.


montoPresupuestal = int(input("ingrese monto presupuestal:"))

print("Pediatria recibira: $"+ str(montoPresupuestal*0.6))
print("Traumatologia recibira: $"+ str(montoPresupuestal*0.2))
print("Kinesiologia recibira: $"+ str(montoPresupuestal*0.2))