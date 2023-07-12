import sys
import heapq

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = [[] for _ in range(num_vertices)]

    def agregar_arista(self, origen, destino, peso):
        self.grafo[origen].append((destino, peso))

    def dijkstra(self, origen):
        distancias = [sys.maxsize] * self.num_vertices
        distancias[origen] = 0

        heap = [(0, origen)]

        while heap:
            distancia_actual, nodo_actual = heapq.heappop(heap)

            if distancia_actual > distancias[nodo_actual]:
                continue

            for vecino, peso in self.grafo[nodo_actual]:
                distancia = distancia_actual + peso

                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(heap, (distancia, vecino))

        return distancias

# Ejemplo de uso
if __name__ == "__main__":
    num_vertices = 6
    grafo = Grafo(num_vertices)

    grafo.agregar_arista(0, 1, 4)
    grafo.agregar_arista(0, 2, 2)
    grafo.agregar_arista(1, 2, 1)
    grafo.agregar_arista(1, 3, 5)
    grafo.agregar_arista(2, 3, 8)
    grafo.agregar_arista(2, 4, 10)
    grafo.agregar_arista(3, 4, 2)
    grafo.agregar_arista(3, 5, 6)
    grafo.agregar_arista(4, 5, 3)

    origen = 0
    distancias = grafo.dijkstra(origen)

    print(f"Distancias más cortas desde el nodo {origen}:")
    for i, distancia in enumerate(distancias):
        print(f"Nodo {i}: {distancia}")
