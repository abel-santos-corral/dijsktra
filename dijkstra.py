"""
dijsktra.py

Este script implementa el algoritmo de Dijkstra para encontrar las distancias más
cortas desde un nodo de inicio hasta todos los demás nodos en un grafo ponderado.

Funciones:
- dijkstra(grafo, inicio): Implementa el algoritmo de Dijkstra para calcular las
  distancias más cortas desde un nodo origen a todos los demás nodos en el grafo.

Uso:
Este script se utiliza para calcular las rutas más cortas en un grafo, lo cual es
útil para problemas de optimización de rutas y análisis de redes.

Ejemplo:
Se utiliza un grafo de ejemplo y se calculan las distancias más cortas desde un
nodo de inicio especificado.
"""

import heapq

def dijkstra(grafo, inicio):
    """
    Algoritmo de Dijkstra para encontrar las distancias más cortas desde un nodo origen.
    
    Parámetros:
    - grafo (dict): Grafo representado como un diccionario de diccionarios con pesos.
    - inicio (str): Nodo desde el cual se calculan las distancias.
    
    Retorna:
    - tuple: (distancias más cortas, nodos anteriores en el camino más corto)
    """
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    cola_prioridad = [(0, inicio)]  # (distancia, nodo)
    nodos_previos = {}

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                nodos_previos[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancias, nodos_previos

# Grafo de ejemplo representado como diccionario de diccionarios
grafo_pac = {
    'A': {'E': 4, 'D': 6, 'C': 2, 'B': 3},
    'B': {'F': 7, 'G': 5},
    'C': {'H': 3, 'I': 8},
    'D': {'J': 2},
    'E': {'I': 6},
    'F': {'D': 7, 'C': 4},
    'G': {'E': 5, 'J': 3},
    'H': {'F': 9, 'B': 2},
    'I': {'G': 1, 'J': 4},
    'J': {'A': 3}
}

NODO_INICIO = 'H'
distancias_grafo_pac, rutas = dijkstra(grafo_pac, NODO_INICIO)

print("\n" + "*" * 80)
print("*****                             Dijkstra                                 *****")
print("*" * 80)
print("\nDistancias más cortas desde", NODO_INICIO, ":", distancias_grafo_pac)
print("Rutas previas:", rutas)
print("\n" + "*" * 80)
