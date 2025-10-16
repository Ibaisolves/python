# Programa que pide N números positivos y muestra el mayor y el menor

def pedir_entero_positivo(prompt):
    while True:
        try:
            n = int(input(prompt).strip())
            if n > 0:
                return n
            print("Introduce un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Introduce un entero.")

def pedir_numero_positivo(prompt):
    while True:
        try:
            x = float(input(prompt).strip())
            if x > 0:
                return x
            print("Introduce un número positivo.")
        except ValueError:
            print("Entrada no válida. Introduce un número.")

def main():
    cantidad = pedir_entero_positivo("¿Cuántos números vas a introducir?: ")
    menor = None
    mayor = None

    for i in range(1, cantidad + 1):
        num = pedir_numero_positivo(f"Introduce el número {i}: ")
        if menor is None or num < menor:
            menor = num
        if mayor is None or num > mayor:
            mayor = num

    print(f"Mayor: {mayor:g}")
    print(f"Menor: {menor:g}")

if __name__ == "__main__":
    main()