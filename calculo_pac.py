#!/usr/bin/env python3
"""
Programa de búsqueda en grafos que implementa tres algoritmos:
- Búsqueda de Costo Uniforme (Dijkstra)
- Búsqueda Ávida (Greedy Best-First Search)
- Búsqueda A* (A-Star Search)

El programa encuentra la mejor ruta desde un nodo de inicio hasta
un nodo objetivo en un grafo ponderado.
"""

import heapq

# Grafo representado como lista de adyacencia con pesos
GRAFO = {
    'A': [('E', 4), ('D', 6), ('C', 2), ('B', 3)],
    'B': [('F', 7), ('G', 5)],
    'C': [('H', 3), ('I', 8)],
    'D': [('J', 2)],
    'E': [('I', 6)],
    'F': [('D', 7), ('C', 4)],
    'G': [('E', 5), ('J', 3)],
    'H': [('F', 9), ('B', 2)],
    'I': [('G', 1), ('J', 4)],
    'J': [('A', 3)]
}

# Heurística estimada para Greedy y A*
HEURISTICA = {
    'A': 10, 'B': 9, 'C': 7, 'D': 8, 'E': 6,
    'F': 5, 'G': 4, 'H': 3, 'I': 2, 'J': 0  # La meta siempre tiene heurística 0
}

INICIO, META = 'H', 'J'

def busqueda_costo_uniforme(grafo, inicio, meta):
    """
    Implementa la Búsqueda de Costo Uniforme (Dijkstra) para encontrar el camino de menor costo.
    
    Parámetros:
    - grafo (dict): Representación del grafo como lista de adyacencia con pesos.
    - inicio (str): Nodo de inicio.
    - meta (str): Nodo objetivo.
    
    Retorna:
    - tuple: (lista del camino encontrado, costo total)
    """
    cola = [(0, inicio, [])]  # (costo, nodo, camino)
    visitados = set()

    while cola:
        costo, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        camino = camino + [nodo]
        if nodo == meta:
            return camino, costo

        for vecino, peso in grafo.get(nodo, []):
            if vecino not in visitados:
                heapq.heappush(cola, (costo + peso, vecino, camino))

    return None, float('inf')

def busqueda_primero_mejor(grafo, inicio, meta, heuristica):
    """
    Implementa la Búsqueda Ávida (Greedy Best-First Search), ahora también devuelve el costo total.
    
    Parámetros:
    - grafo (dict): Representación del grafo como lista de adyacencia con pesos.
    - inicio (str): Nodo de inicio.
    - meta (str): Nodo objetivo.
    - heuristica (dict): Diccionario con valores heurísticos estimados para cada nodo.
    
    Retorna:
    - tuple: (lista del camino encontrado, costo total)
    """
    cola = [(heuristica[inicio], 0, inicio, [])]  # (heurística, costo, nodo, camino)
    visitados = set()

    while cola:
        _, costo, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        camino = camino + [nodo]
        if nodo == meta:
            return camino, costo

        for vecino, peso in grafo.get(nodo, []):
            if vecino not in visitados:
                heapq.heappush(cola, (heuristica[vecino], costo + peso, vecino, camino))

    return None, float('inf')

def busqueda_a_estrella(grafo, inicio, meta, heuristica):
    """
    Implementa la Búsqueda A* (A-Star Search).
    
    Parámetros:
    - grafo (dict): Representación del grafo como lista de adyacencia con pesos.
    - inicio (str): Nodo de inicio.
    - meta (str): Nodo objetivo.
    - heuristica (dict): Diccionario con valores heurísticos estimados para cada nodo.
    
    Retorna:
    - tuple: (lista del camino encontrado, costo total)
    """
    cola = [(heuristica[inicio], 0, inicio, [])]  # (f, g, nodo, camino)
    visitados = {}

    while cola:
        f, g, nodo, camino = heapq.heappop(cola)

        if nodo in visitados and visitados[nodo] <= g:
            continue
        visitados[nodo] = g

        camino = camino + [nodo]
        if nodo == meta:
            return camino, g

        for vecino, peso in grafo.get(nodo, []):
            nuevo_g = g + peso
            nuevo_f = nuevo_g + heuristica[vecino]
            heapq.heappush(cola, (nuevo_f, nuevo_g, vecino, camino))

    return None, float('inf')

# Ejecutar búsquedas
ruta_ucs, costo_ucs = busqueda_costo_uniforme(GRAFO, INICIO, META)
ruta_greedy, costo_greedy = busqueda_primero_mejor(GRAFO, INICIO, META, HEURISTICA)
ruta_a_estrella, costo_a_estrella = busqueda_a_estrella(GRAFO, INICIO, META, HEURISTICA)

# Imprimir resultados con formato
print("\n" + "*" * 80)
print("*****                             Calculo PAC 1                            *****")
print("*" * 80)
print("\nBúsqueda de Costo Uniforme - Ruta:", ruta_ucs)
print("Búsqueda de Costo Uniforme - Costo:", costo_ucs)
print("\n" + "-" * 80 + "\n")
print("Búsqueda Ávida - Ruta:", ruta_greedy)
print("Búsqueda Ávida - Costo:", costo_greedy)
print("\n" + "-" * 80 + "\n")
print("Búsqueda A* - Ruta:", ruta_a_estrella)
print("Búsqueda A* - Costo:", costo_a_estrella)
print("\n" + "*" * 80)
