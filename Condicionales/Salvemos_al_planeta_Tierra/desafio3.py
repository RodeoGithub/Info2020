#Para el uso de fertilizantes es necesario medir un determinado compuesto en el suelo el cual debe 
#existir en una cantidad de al menos 10 partes por millon por hectárea, y no debe existir vegetación 
#del tipo MATORRAL. Escribir un programa que determine si es factible la utilización de dicho fertilizante.

compuesto = float(input("Ingrese la cantidad de compuesto por millon en el suelo por hectarea: "))

if(input("Existe vegetacion de tipo matorral? SI/NO: ").lower()=="si"):
    matorral=True
else:
    matorral=False

if(compuesto>=10 and not matorral):
    print("Es factible la utilizacion de fertilizante")
else: 
    print("No es factible la utilizacion de fertilizante")
