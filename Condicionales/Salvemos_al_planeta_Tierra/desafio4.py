#Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

#   Ingredientes comunes: Verduras y berenjena.
#   Ingredientes Receta 1: Lentejas y apio.
#   Ingredientes Receta 2: Morrón y Cebolla..

#Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre 
# un menú con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente 
# (entre la receta elegida y los comunes.) y el tipo de receta. 
# Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes.

print("Elija una receta:", end='\n')
print("Receta 1: Lentejas y apio.", end='\n')
print("Receta 2: Morrón y Cebolla", end='\n')

if(int(input())==1):
    print("Puede elegir 3 ingredientes:", "-Lentejas" ,  "-Apio", "-Verduras", "-Berenjena", sep='\n')
    eleccion=input()
    print("Usted eligió la receta 1 con: " + eleccion)
else:
    print("Puede elegir 3 ingredientes:", "-Morrón" ,  "-Cebolla", "-Verduras", "-Berenjena", sep='\n')
    eleccion=input()
    print("Usted eligió la receta 2 con: " + eleccion)

