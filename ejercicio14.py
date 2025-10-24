#Lista de numeros introducidos por el usuario
datos= []
for i in range(4):
    datos.append(int(input("Introduce un numero: ")))

#Lista invertida
datos_invertidos = datos[::-1]
print("Lista invertida:", datos_invertidos)
