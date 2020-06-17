#Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la 
# estatura media de las personas adultas de su sexo, siendo:
# - estatura media de mujeres adultas: 1,65 m.
# - estatura media de varones adultos: 1,72 m.

s = input("Ingrese su sexo (M/F): ")

estatura = int(input("Ingrese su estatura (en cm): "))

if(s.lower()=="m"):
    if(estatura>165):
        print("Esta por encima de la media!")
    else:
        print("Esta por debajo de la media :(")
else:
    if(estatura>172):
        print("Esta por encima de la media!")
    else:
        print("Esta por debajo de la media :(")
