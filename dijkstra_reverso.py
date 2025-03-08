"""
dijsktra_reverso.py

Este script implementa el algoritmo de Dijkstra en un grafo invertido para encontrar
las distancias más cortas desde un nodo final hasta todos los demás nodos.

Funciones:
- invertir_grafo(grafo): Invierte las direcciones de un grafo dirigido.
- dijkstra(grafo, inicio): Implementa el algoritmo de Dijkstra para encontrar las
  distancias más cortas desde un nodo origen.

Uso:
Este script se utiliza para calcular las rutas más cortas en un grafo invertido,
lo cual es útil para problemas donde se necesita conocer el camino más corto hacia
un nodo objetivo desde cualquier otro nodo.

Ejemplo:
Se utiliza un grafo de ejemplo y se calculan las distancias más cortas hacia un nodo
final especificado.
"""

import heapq

def invertir_grafo(grafo):
    """
    Invierte las direcciones de un grafo dirigido.
    
    Parámetros:
    - grafo (dict): Grafo representado como un diccionario de diccionarios.
    
    Retorna:
    - dict: Grafo invertido.
    """
    grafo_invertido = {nodo: {} for nodo in grafo}
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            grafo_invertido[vecino][nodo] = peso
    return grafo_invertido

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

NODO_FINAL = 'J'
grafo_invertido_pac = invertir_grafo(grafo_pac)
distancias_grafo_pac, rutas = dijkstra(grafo_invertido_pac, NODO_FINAL)

print("\n" + "*" * 80)
print("*****                           Dijkstra Reverso                           *****")
print("*" * 80)
print("\nDistancias más cortas hacia", NODO_FINAL, ":", distancias_grafo_pac)
print("Rutas previas:", rutas)
print("\n" + "*" * 80)
