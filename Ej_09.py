from collections import deque

def shortest_path(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos: derecha, izquierda, abajo, arriba

    queue = deque([(start, 0, [])])  # (coordenadas, distancia, ruta)
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), dist, path = queue.popleft()

        if (x, y) == goal:
            return path + [(x, y)]  # Ruta encontrada

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and maze[new_x][new_y] == 0:
                visited[new_x][new_y] = True
                queue.append(((new_x, new_y), dist + 1, path + [(x, y)]))

    return None  # No se encontró una ruta

# Ejemplo de uso:
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
goal = (4, 4)

path = shortest_path(maze, start, goal)
if path:
    print("Ruta más corta:")
    for step in path:
        print(step)
else:
    print("No se encontró una ruta válida.")
