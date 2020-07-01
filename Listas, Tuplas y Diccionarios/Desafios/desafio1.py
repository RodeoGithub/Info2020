
n = input("Ingrese su nombre:")
puntaje = int(input("Ingrese cuanto sabe de contaminacion del 1 al 10:\n"))
sigue = input("Quiere seguir? Si/No\n")
dic = { n : puntaje}
while(sigue.lower()=="si"):
    n = input("Ingrese su nombre")
    puntaje = int(input("Ingrese cuanto sabe de contaminacion del 1 al 10:\n"))
    
    sigue = input("Quiere seguir? Si/No\n")