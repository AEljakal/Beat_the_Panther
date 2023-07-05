def crear_peluche(n, m):
    if n % 2 == 0:  # Verificar que N sea un número natural impar
        raise ValueError("N debe ser un número natural impar.")
    if m != 3 * n:  # Verificar que M sea 3 veces N
        raise ValueError("M debe ser igual a 3 veces N.")

    centro = m // 2  # Obtener la posición del centro

    for i in range(n):
        for j in range(m):
            if j == centro - len('BIENVENIDO') // 2:  # Posicionar 'BIENVENIDO' en el centro
                print('BIENVENIDO', end='')
                j += len('BIENVENIDO')
            if j == centro:
                print('|', end='')
            elif j < centro:
                print('.', end='')
            else:
                print('-', end='')
        print()

# Ejemplo de uso
N = 7  # Tamaño del peluche en filas (número impar)
M = 21  # Tamaño del peluche en columnas (3 veces N)
crear_peluche(N, M)
