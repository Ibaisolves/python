print("Adivina el numero secreto")
numero_secreto = 7
adivinar = int(input("Introduce un numero entre 1 y 10: "))
intentos = 3
while adivinar != numero_secreto and intentos > 0:
    if adivinar > numero_secreto:
        print("Demasiado alto")
    else:
        print("Demasiado bajo")
    intentos -= 1
    if intentos > 0:
        adivinar = int(input("Introduce otro numero: "))
    adivinar = int(input("Introduce otro numero: ")) ; import random
if intentos == 0:
    print("Has perdido. El numero secreto era:", numero_secreto)
else:
    print("¡Has adivinado el numero secreto!")