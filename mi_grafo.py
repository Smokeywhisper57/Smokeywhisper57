import networkx as nx
import matplotlib.pyplot as plt
class Grafo:
    def __init__(self):
        # Diccionario que almacena vértices y aristas con pesos
        self.grafo = {
            'Coatepec': {'5': 3, '7': 5, '8': 2},
            'Nueva': {'8': 4, 'Xalapa': 6},
            '4': {'9': 1, 'Xalapa': 3},
            '6': {'Briones': 2, 'Xalapa': 4},
            '7': {'11': 2, 'Coatepec': 5},
            '8': {'Coatepec': 2, 'Nueva': 4},
            '9': {'4': 1, '10': 7},
            '10': {'9': 7, '11': 3},
            '11': {'10': 3, '7': 2},
            'Xalapa': {'6': 4, '4': 3, 'Nueva': 6},
            '5': {'Briones': 3}
        }
    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, peso=1):
        # Grafo no dirigido con peso en la arista
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1][vertice2] = peso
            self.grafo[vertice2][vertice1] = peso

    def mostrar_grafo(self):
        for vertice, adyacentes in self.grafo.items():
            print(f"{vertice} -> {adyacentes}")

    def dibujar_grafo(self):
        G = nx.Graph()
        
        # Añadir nodos y aristas con pesos
        for vertice, adyacentes in self.grafo.items():
            for adyacente, peso in adyacentes.items():
                G.add_edge(vertice, adyacente, weight=peso)

        pos = nx.spring_layout(G)  # Posiciones para los nodos
        plt.figure(figsize=(15, 15))
        nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)
        nx.draw_networkx_edges(G, pos, edge_color='gray')
        nx.draw_networkx_labels(G, pos, font_size=10)
        
        # Dibujar los pesos de las aristas
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        plt.title("Visualización del Grafo con Pesos")
        plt.show()