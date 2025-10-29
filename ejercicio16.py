def leer_entero(prompt):
    while True:
        try:
            v = int(input(prompt))
            return v
        except ValueError:
            print("Entrada no válida. Introduce un entero.")

def leer_fila(n, fila_num):
    while True:
        entrada = input(f"Introduce la fila {fila_num} con {n} enteros separados por espacios: ").strip()
        partes = entrada.split()
        if len(partes) != n:
            print(f"Tienes que introducir exactamente {n} valores.")
            continue
        try:
            return [int(x) for x in partes]
        except ValueError:
            print("Todos los valores deben ser enteros.")

def es_identidad(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if i == j:
                if mat[i][j] != 1:
                    return False
            else:
                if mat[i][j] != 0:
                    return False
    return True

def main():
    n = 0
    while n <= 0:
        n = leer_entero("Introduce el tamaño N de la matriz (entero positivo): ")
        if n <= 0:
            print("N debe ser un entero positivo.")

    matriz = []
    for i in range(1, n+1):
        matriz.append(leer_fila(n, i))

    print("\nMatriz introducida:")
    for fila in matriz:
        print(" ".join(str(x) for x in fila))

    if es_identidad(matriz):
        print("\nLa matriz SÍ es una matriz identidad.")
    else:
        print("\nLa matriz NO es una matriz identidad.")

if __name__ == "__main__":
    main()
def leer_entero(prompt):
    while True:
        try:
            v = int(input(prompt))
            return v
        except ValueError:
            print("Entrada no válida. Introduce un entero.")

def leer_fila(n, fila_num):
    while True:
        entrada = input(f"Introduce la fila {fila_num} con {n} enteros separados por espacios: ").strip()
        partes = entrada.split()
        if len(partes) != n:
            print(f"Tienes que introducir exactamente {n} valores.")
            continue
        try:
            return [int(x) for x in partes]
        except ValueError:
            print("Todos los valores deben ser enteros.")

def es_identidad(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if i == j:
                if mat[i][j] != 1:
                    return False
            else:
                if mat[i][j] != 0:
                    return False
    return True

def main():
    n = 0
    while n <= 0:
        n = leer_entero("Introduce el tamaño N de la matriz (entero positivo): ")
        if n <= 0:
            print("N debe ser un entero positivo.")

    matriz = []
    for i in range(1, n+1):
        matriz.append(leer_fila(n, i))

    print("\nMatriz introducida:")
    for fila in matriz:
        print(" ".join(str(x) for x in fila))

    if es_identidad(matriz):
        print("\nLa matriz SÍ es una matriz identidad.")
    else:
        print("\nLa matriz NO es una matriz identidad.")

if __name__ == "__main__":
    main()  