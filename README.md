# Dijsktra

Repositorio para programas de apoyo para PEC 1:

- Cálculo de Dijkstra hasta un nodo dado
- Cálculo de Dijkstra reverso desde un nodo dado
- Cálculo de los algoritmos de busqueda uniforme, Ávida y A*

# Ejecución

## Requerimiento

Se requiere tener instalado Python para poder ejecutar los programas.

## Ejecución main.py

Lanzar la ejecución con:

```
python3 main.py
```

Al ejecutar este programa se lanza en orden la ejecución de:

- dijkstra.py
- dijkstra_reverso.py
- calculo_pac.py

Y se presenta el resultado por pantalla de los programas.

Ver la sección [Programas](#programas) para la especificación.

## Ejecución programas individualmente

Para lanzar los programas individualmente se puede usar cualquiera de las instrucciones:

```
python3 dijkstra.py
python3 dijkstra_reverso.py 
python3 calculo_pac.py 
```

# Programas

## dijkstra.py

### Objetivo

El objetivo de este programa es encontrar la distancia más corta desde un nodo dado (en el caso de PEC1 era el H).

El programa devuelve una lista de las distancias más cortas desde H y las rutas previas.

Para la PEC1 teníamos que realizar la búsqueda uniforme, la búsqueda ávida y la búquesa A*. Vemos que el resultado de Dijkstra de H --> J da un coste de 10, lo que encaja con el resultado de la búsqueda uniforme y la búsqueda usando el algoritmo A*.

## dijkstra_reverso.py 

El objetivo de este programa es encontrar la distancia más corta hasta un nodo dado (en el caso de PEC1 era el J).

El programa devuelve una lista de las distancias más cortas hacia J y las rutas previas.

El resultado sirvió para estudiar y tener una idea de si el heurístico dado podía ser correcto. 

Aquí se podía ver que para H --> J el coste era 10, lo que cuadraba con el resultado de la búsqueda uniforme y el algoritmo A*. 

Y también vemos que mientras que heurístico tenia H(A) = 10 aquí el valor era de 8. 

## calculo_pac.py 

Este programa es el más delicado, porque realiza las búsquedas uniforme, ávida y con algoritmo A*.

La idea de realizar este programa era comprobar si el cálculo realizado a mano a partir de lo aprendido en el módulo 2 se avenía con el resultado.

Este programa es interesante en cuanto muestra una implementación con lista de adyacencia para representar un grafo. La lista del heurístico se introduce en el programa y finalmente se tiene como parámetros de nodo inicial y nodo final a H y J respectivamente.

La idea parece interesante en cuanto se puede introducir otro grafo en la lista de adyacencia, otro heurístico y dados nuevos nodos inicial y final, realizar los cálculos.

# Bibliografía 

Los programas se han realizado con la ayuda de:

* [Mistral](https://chat.mistral.ai/chat)
* [ChatGPT - Python](https://chatgpt.com/g/g-cKXjWStaE-python)


