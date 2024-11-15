from graforecorridos import *

# Definición de los nodos
a, b, c, d, e, f, g, h = "a", "b", "c", "d", "e", "f", "g", "h"

# Crear el grafo
grafo = Grafo()

# Agregar los nodos al grafo
agregar(grafo, a)
agregar(grafo, b)
agregar(grafo, c)
agregar(grafo, d)
agregar(grafo, e)
agregar(grafo, f)
agregar(grafo, g)
agregar(grafo, h)

# Establecer las relaciones entre los nodos
relacionar(grafo, a, c, 1)
relacionar(grafo, a, b, 3)
relacionar(grafo, b, d, 1)
relacionar(grafo, b, g, 5)
relacionar(grafo, c, f, 5)
relacionar(grafo, c, d, 2)
relacionar(grafo, d, f, 2)
relacionar(grafo, d, e, 4)
relacionar(grafo, e, h, 1)
relacionar(grafo, e, g, 2)
relacionar(grafo, f, h, 3)

print(caminoMinimo(grafo, e, a))