import random
import time

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 1
    inicio = time.time()

    print("¡Bienvenido al juego de Adivina el Número!")
    print("He seleccionado un número secreto entre 1 y 100.")
    print("Escribe 'salir' para terminar en cualquier momento.\n")

    while True:
        entrada = input("Introduce tu adivinanza (1-100): ")
        if entrada.lower() in ("salir", "exit", "quit"):
            print(f"Has salido. El número secreto era {numero_secreto}.")
            break
        try:
            adivinanza = int(entrada)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if adivinanza < 1 or adivinanza > 100:
            print("Por favor, introduce un número entre 1 y 100.")
            continue

        intentos += 1

        if adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
            time.sleep(0.4)
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
            time.sleep(0.4)
        else:
            duracion = time.time() - inicio
            print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
            print(f"Tiempo empleado: {duracion:.2f} segundos.")
            break

if __name__ == "__main__":
    adivina_el_numero()
