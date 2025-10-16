total = 0.0

while True:
    try:
        precio = float(input("Introduce el precio (Escribe 0 para terminar): ").strip())
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        continue

    if precio == 0:
        break

    total += precio

print(f"Total factura: {total:.2f} €")