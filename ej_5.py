def generar_espiral(dimension: int):
    matriz = [[0] * dimension for _ in range(dimension)]
    num = 1  # Inicializar el número a insertar en la matriz
    inicio_fila, inicio_columna = 0, 0  # Índices de inicio de la fila y columna
    fin_fila, fin_columna = (
        dimension - 1,
        dimension - 1,
    )  # Índices de fin de la fila y columna

    while num <= dimension * dimension:
        # Llenar fila superior de izquierda a derecha
        for i in range(inicio_columna, fin_columna + 1):
            matriz[inicio_fila][i] = num
            num += 1
        inicio_fila += 1

        # Llenar columna derecha de arriba hacia abajo
        for i in range(inicio_fila, fin_fila + 1):
            matriz[i][fin_columna] = num
            num += 1
        fin_columna -= 1

        # Llenar fila inferior de derecha a izquierda
        for i in range(fin_columna, inicio_columna - 1, -1):
            matriz[fin_fila][i] = num
            num += 1
        fin_fila -= 1

        # Llenar columna izquierda de abajo hacia arriba
        for i in range(fin_fila, inicio_fila - 1, -1):
            matriz[i][inicio_columna] = num
            num += 1
        inicio_columna += 1

    return matriz


def mostrar_matriz(matriz) -> None:
    for fila in matriz:
        print(fila, end="\n")
    print()


dimension = int(input("Ingrese la dimencion, un entero positivo: "))
espiral = generar_espiral(dimension)
mostrar_matriz(espiral)
