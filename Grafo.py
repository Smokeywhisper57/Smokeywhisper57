#Crea clase grafo 
class Grafo:
    #Crea una funcion la cual hace una libreria
    def __init__(self):
        #Declara un grafo como un diccionario vacio
        self.grafo = {}
    #crea una funcion la cual recibe un vertice
    def agregar_vertice(self, vertice):
        #si el vertice no
        if vertice not in self.grafo:
            #hace un grafo con un vertice
            self.grafo[vertice] = []

    #crea un arista la cual necesita 2 vertices
    def agregar_arista(self, vertice1, vertice2):
        # Grafo no dirigido
        if vertice1 in self.grafo and vertice2 in self.grafo:
            #Agrega el vertice2 al final de la lista de vertice1
            self.grafo[vertice1].append(vertice2)
            #Agrega el vertice1 al final de la lista de vertice2
            self.grafo[vertice2].append(vertice1)

    #funcion que muestra los grafos que hay en el objeto
    def mostrar_grafo(self):
        #busca todos los grafos y los imprime
        for vertice in self.grafo:
            #Se imprime el grafo
            print(f"{vertice} -> {self.grafo[vertice]}")

# Ejemplo de uso
mi_grafo = Grafo()
mi_grafo.agregar_vertice('A')
mi_grafo.agregar_vertice('B')
mi_grafo.agregar_vertice('C')
mi_grafo.agregar_arista('A', 'B')
mi_grafo.agregar_arista('A', 'C')
mi_grafo.mostrar_grafo()
