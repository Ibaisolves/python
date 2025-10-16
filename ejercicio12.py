numeros=str(input("Ingrese una serie de numeros separados por espacios: "))

partes=numeros.split()

suma=0
for numeros in partes:
    suma+=int(numeros)
print("La suma de los numeros es:", suma)