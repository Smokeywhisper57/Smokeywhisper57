import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight=None, directed=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1][vertex2] = weight
        if not directed:
            self.graph[vertex2][vertex1] = weight

    def mostrar_grafo(self):
        for vertice, adyacentes in self.graph.items():
            print(f"{vertice} -> {adyacentes}")

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"Vértice {vertex} tiene como conexiones a:")
            for neighbor, weight in edges.items():
                if weight:
                    print(f"  - {neighbor} (peso: {weight})")
                else:
                    print(f"  - {neighbor}")

    def to_networkx_graph(self):
        DG = nx.Graph()  # Usa nx.DiGraph() si el grafo es dirigido
        for vertex, edges in self.graph.items():
            for neighbor, weight in edges.items():
                if weight:
                    DG.add_edge(vertex, neighbor, weight=weight)
                else:
                    DG.add_edge(vertex, neighbor)
        return DG

    def mostrar(self):
        DG = self.to_networkx_graph()
        nx.draw_circular(
            DG,
            node_color="lightblue",
            edge_color="gray",
            font_size=24,
            width=2,
            with_labels=True,
            node_size=3500
        )
        plt.show()

# Ejemplo de uso
g = Graph()
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

for vertex in vertices:
    g.add_vertex(vertex)

g.add_edge('A', 'B', weight=5)
g.add_edge('A', 'C', weight=2)
g.add_edge('B', 'C', weight=1)
g.add_edge('B', 'D', weight=4)
g.add_edge('C', 'D', weight=3)
g.add_edge('C', 'E', weight=6)
g.add_edge('D', 'E', weight=7)
g.add_edge('E', 'F', weight=8)

g.mostrar_grafo()
g.display()
g.mostrar()
