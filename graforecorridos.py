from collections import deque
from functools import reduce
import networkx as nx
import matplotlib.pyplot as plt
from functools import reduce


class Grafo(object):
    def __init__(self):
        self.relaciones = {}

    def __str__(self):
        return str(self.relaciones)


    def dibujar_grafo(self):
        # Crear un objeto de grafo dirigido de NetworkX
        G = nx.DiGraph()
        
        # Añadir nodos y aristas con pesos
        for vertice, adyacentes in self.relaciones.items():
            for adyacente in adyacentes:
                G.add_edge(vertice, adyacente['elemento'], weight=adyacente['peso'])
        
        # Dibujar el grafo
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(G, seed=42)  # Layout para mejorar visualización
        
        # Dibujar nodos y aristas
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray',
                node_size=700, font_size=10, font_weight='bold', arrows=True, connectionstyle='arc3,rad=0.1')
        
        # Obtener pesos de las aristas
        edge_labels = nx.get_edge_attributes(G, 'weight')
        
        # Dibujar etiquetas de los pesos
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=9)
        
        plt.title("Visualización del Grafo Dirigido con Pesos")
        plt.show()


def agregar(grafo, elemento):
    grafo.relaciones[elemento] = []

def relacionar(grafo, elemento1, elemento2, peso):
    relacionarUnilateral(grafo, elemento1, elemento2, peso)
    relacionarUnilateral(grafo, elemento2, elemento1, peso)

def relacionarUnilateral(grafo, origen, destino, peso):
    grafo.relaciones[origen].append({'elemento': destino, 'peso': peso})

def imprimir(elemento):
    print(elemento)

def anchoPrimero(grafo, elementoInicial, funcion, cola=deque(), elementosRecorridos=[]):
    if elementoInicial not in elementosRecorridos:
        funcion(elementoInicial)
        elementosRecorridos.append(elementoInicial)
        if len(grafo.relaciones[elementoInicial]) > 0:
            cola.extend([relacion['elemento'] for relacion in grafo.relaciones[elementoInicial]])
    if len(cola) != 0:
        anchoPrimero(grafo, cola.popleft(), funcion, cola, elementosRecorridos)

def caminoMinimo(grafo, origen, destino):
    etiquetas = {origen: (0, None)}
    dijkstra(grafo, destino, etiquetas, [])
    return construirCamino(etiquetas, origen, destino)

def construirCamino(etiquetas, origen, destino):
    if origen == destino:
        return [origen]
    return construirCamino(etiquetas, origen, anterior(etiquetas[destino])) + [destino]

def dijkstra(grafo, destino, etiquetas, procesados):
    nodoActual = menorValorNoProcesado(etiquetas, procesados)
    if nodoActual == destino:
        return
    procesados.append(nodoActual)
    for vecino in vecinoNoProcesado(grafo, nodoActual, procesados):
        generarEtiqueta(grafo, vecino['elemento'], nodoActual, etiquetas)
    dijkstra(grafo, destino, etiquetas, procesados)

def generarEtiqueta(grafo, nodo, anterior, etiquetas):
    etiquetaNodoAnterior = etiquetas[anterior]
    etiquetaPropuesta = (peso(grafo, anterior, nodo) + acumulado(etiquetaNodoAnterior), anterior)
    if nodo not in etiquetas or acumulado(etiquetaPropuesta) < acumulado(etiquetas[nodo]):
        etiquetas[nodo] = etiquetaPropuesta

def aristas(grafo, nodo):
    return grafo.relaciones[nodo]

def vecinoNoProcesado(grafo, nodo, procesados):
    aristasDeVecinosNoProcesados = filter(lambda x: x['elemento'] not in procesados, aristas(grafo, nodo))
    return list(aristasDeVecinosNoProcesados)

def peso(grafo, nodoOrigen, nodoDestino):
    arista = next((ar for ar in grafo.relaciones[nodoOrigen] if ar['elemento'] == nodoDestino), None)
    return arista['peso'] if arista else float('inf')

def acumulado(etiqueta):
    return etiqueta[0]

def anterior(etiqueta):
    return etiqueta[1]

def menorValorNoProcesado(etiquetas, procesados):
    etiquetadosSinProcesar = filter(lambda nodo_acum: nodo_acum[0] not in procesados, etiquetas.items())
    return min(etiquetadosSinProcesar, key=lambda nodo_acum: nodo_acum[1][0])[0]

