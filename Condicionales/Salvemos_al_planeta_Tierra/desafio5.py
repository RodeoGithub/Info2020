#La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y 
# el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
# La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y 
# los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
# Debemos hacer un programa que dado el nombre del barrio y la ubicación, 
# nos informe en que sección se encuentra.

tipoDeBarrio = input("Ingrese la ubicación del barrio (CÉNTRICO / NO CÉNTRICO): ")
nombreDelBarrio = input("Ingrese el nombre del barrio: ")

if(tipoDeBarrio=="CÉNTRICO"):
    if(nombreDelBarrio[0].lower()<"m"):
        seccionA=True
    else:
        seccionA=False
else:
    if(nombreDelBarrio[0].lower()>"m"):
        seccionA=True
    else:
        seccionA=False

if(seccionA):
    print("Su barrio se encuentra en la seccion A")
else:
    print("Su barrio se encuentra en la seccion B")