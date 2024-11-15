import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = {}
    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    def agregar_arista(self, vertice1, vertice2):
        # Grafo no dirigido
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append(vertice2)
            self.grafo[vertice2].append(vertice1)
    def mostrar_grafo(self):
        for vertice in self.grafo:
            print(f"{vertice} -> {self.grafo[vertice]}")
        
    def dibujar_grafo(self):
        # Crear un objeto de grafo de NetworkX
        G = nx.Graph()
        
        # Añadir nodos y aristas
        for vertice, adyacentes in self.grafo.items():
            for adyacente in adyacentes:
                G.add_edge(vertice, adyacente)
        
        # Dibujar el grafo
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(G, seed=42)  # Layout para mejorar visualización
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', 
                node_size=700, font_size=10, font_weight='bold')
        
        plt.title("Visualización del Grafo")
        plt.show()
# Ejemplo de uso
mi_grafo = Grafo()

#coatepec-sauces
mi_grafo.agregar_vertice('SAUCES')
    #paradas
mi_grafo.agregar_vertice('SC1')#calle bolivia
mi_grafo.agregar_vertice('SC2')#fasti
mi_grafo.agregar_vertice('SC3')#circuitos presidentes
mi_grafo.agregar_vertice('SC4')#DIF
mi_grafo.agregar_vertice('SC5')#Autohotel
mi_grafo.agregar_vertice('SC5')#arenales
mi_grafo.agregar_vertice('SC6')#parque pequeño
mi_grafo.agregar_vertice('SC7')#desviacion a pacho
mi_grafo.agregar_vertice('SC8')#plaza orquideas
mi_grafo.agregar_vertice('SC9')#entrada coatepec
mi_grafo.agregar_vertice('SC10')#parada intermedia
mi_grafo.agregar_vertice('COATEPEC')
#coatepec a Americas---------------------------------------------------------------------------------------------------------------------
    #coatepec-la coca
#coatepec
mi_grafo.agregar_vertice('CC1')#dif
mi_grafo.agregar_vertice('CC2')#fasti
mi_grafo.agregar_vertice('CC3')
mi_grafo.agregar_vertice('CC4')
mi_grafo.agregar_vertice('CC5')
mi_grafo.agregar_vertice('LA COCA')
    #lacoca-mundo nuevo
#la coca
mi_grafo.agregar_vertice('MC1')
mi_grafo.agregar_vertice('MUNDO NUEVO')
    #Mundo nuevo-casasgeo
#Mundo nuevo
mi_grafo.agregar_vertice('CM1')
mi_grafo.agregar_vertice('CM2')
mi_grafo.agregar_vertice('CM3')
mi_grafo.agregar_vertice('CASAS GEO')
    #lacoca-elgrande
#lacoca
mi_grafo.agregar_vertice('EC1')
mi_grafo.agregar_vertice('EC2')
mi_grafo.agregar_vertice('EL GRANDE')
    #elgrande-mahuixtlan
#elgrande
mi_grafo.agregar_vertice('ME1')
mi_grafo.agregar_vertice('MAHUIXTLAN')
    #mahuixtlan-puerto rico
#mahuixtlan
mi_grafo.agregar_vertice('PM1')
mi_grafo.agregar_vertice('PUENTE DEL DIABLO')
mi_grafo.agregar_vertice('PUERTO RICO')
    #puerto rico-alborada
#puerto rico
mi_grafo.agregar_vertice('AP1')
mi_grafo.agregar_vertice('AP2')
mi_grafo.agregar_vertice('AP3')
mi_grafo.agregar_vertice('ALBORADA')
    #alborada-estanzuela
#alborada
mi_grafo.agregar_vertice('EA1')
mi_grafo.agregar_vertice('EA2')
mi_grafo.agregar_vertice('EA3')
mi_grafo.agregar_vertice('ESTANZUELA')
    #esttanzuela-las trancas
#estanzuela
mi_grafo.agregar_vertice('TE1')
mi_grafo.agregar_vertice('TE2')
mi_grafo.agregar_vertice('TE3')
mi_grafo.agregar_vertice('TE4')
mi_grafo.agregar_vertice('TE5')
mi_grafo.agregar_vertice('TE6')
mi_grafo.agregar_vertice('TE7')
mi_grafo.agregar_vertice('LAS TRANCAS')
    #las trancas-americas
#las trancas
mi_grafo.agregar_vertice('TRA1')
mi_grafo.agregar_vertice('PLAZA AMERICAS')
#sauces a plaza americas---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #sauces-zonauv
#sauces
mi_grafo.agregar_vertice('SZ1')
mi_grafo.agregar_vertice('SZ2')
mi_grafo.agregar_vertice('SZ3')
mi_grafo.agregar_vertice('SZ4')
mi_grafo.agregar_vertice('SZ5')
mi_grafo.agregar_vertice('SZ6')
mi_grafo.agregar_vertice('SZ7')
mi_grafo.agregar_vertice('ZONA UV')
    #zonauv-rebsamen
#zonauv
mi_grafo.agregar_vertice('ZR1')
mi_grafo.agregar_vertice('REBSAMEN')
    #rebsamen-xalapa2000
#rebsamen
mi_grafo.agregar_vertice('RX1')
mi_grafo.agregar_vertice('RX2')
mi_grafo.agregar_vertice('RX3')
mi_grafo.agregar_vertice('XALAPA 2000')
    #xalapa2000-arcosur
mi_grafo.agregar_vertice('XA1')
mi_grafo.agregar_vertice('XA2')
mi_grafo.agregar_vertice('XA3')
mi_grafo.agregar_vertice('XA4')
mi_grafo.agregar_vertice('XA5')
mi_grafo.agregar_vertice('XA6')
mi_grafo.agregar_vertice('ARCO SUR')
    #arcosur-tecnologico
mi_grafo.agregar_vertice('TEA1')
mi_grafo.agregar_vertice('AT2')
mi_grafo.agregar_vertice('AT3')
mi_grafo.agregar_vertice('AT4')
mi_grafo.agregar_vertice('TECNOLOGICO')
    #tecnologico a plaza americas
mi_grafo.agregar_vertice('TA1')
mi_grafo.agregar_vertice('TA2')
mi_grafo.agregar_vertice('TA3')
mi_grafo.agregar_vertice('TA4')


#verde
mi_grafo.agregar_vertice('PLAZA CRISTAL')
mi_grafo.agregar_vertice('URBAN CENTER')
mi_grafo.agregar_vertice('CENTRO')
mi_grafo.agregar_vertice('PLAZA ANIMAS')
mi_grafo.agregar_vertice('TESORERIA')
#mas afuera de coatepec
mi_grafo.agregar_vertice('XICO')
mi_grafo.agregar_vertice('TEOCELO')
mi_grafo.agregar_vertice('SAN MARCOS')
#ruta verde
mi_grafo.agregar_vertice('CBTIS13')
mi_grafo.agregar_vertice('SAMS')
mi_grafo.agregar_vertice('RUIZ CORTINES')
mi_grafo.agregar_vertice('URBAN CENTER')
mi_grafo.agregar_vertice('IMSS')
mi_grafo.agregar_vertice('PLAZA ANIMAS')
mi_grafo.agregar_vertice('ARAUCARIAS')
#fovisste
mi_grafo.agregar_vertice('CENTRO')
"""fovisste
mi_grafo.agregar_arista('ARAUCARIAS', 'CENTRO')
mi_grafo.agregar_arista('SAUCES', 'CENTRO')
#mi_grafo.agregar_arista('ARAUCARIAS', 'SAMS')
mi_grafo.agregar_arista('PLAZA ANIMAS', 'PLAZA AMERCIAS')
verde
mi_grafo.agregar_arista('ARAUCARIAS', 'PLAZA CRISTAL')
mi_grafo.agregar_arista('RUIZ CORTINES', 'TESORERIA')
mi_grafo.agregar_arista('URBAN CENTER', 'TESORERIA')
mi_grafo.agregar_arista('RUIZ CORTINES', 'IMSS')
mi_grafo.agregar_arista('SAUCES', 'IMSS')
mi_grafo.agregar_arista('PLAZA CRISTAL', 'URBAN CENTER')
mi_grafo.agregar_arista('PLAZA AMERICAS', 'SAMS')
mi_grafo.agregar_arista('ARAUCARIAS', 'SAMS')
"""
#plaza americas a coatepec
mi_grafo.agregar_arista('PLAZA AMERICAS', 'TRA1')#1PARADA
mi_grafo.agregar_arista('TRA1', 'LAS TRANCAS')
mi_grafo.agregar_arista('LAS TRANCAS', 'TE1')#7PARADAS
mi_grafo.agregar_arista('TE1', 'TE2')
mi_grafo.agregar_arista('TE2', 'TE3')
mi_grafo.agregar_arista('TE3', 'TE4')
mi_grafo.agregar_arista('TE4', 'TE5')
mi_grafo.agregar_arista('TE5', 'TE6')
mi_grafo.agregar_arista('TE6', 'TE7')
mi_grafo.agregar_arista('TE7', 'ESTANZUELA')#
mi_grafo.agregar_arista('ESTANZUELA', 'EA1')#3PARADAS
mi_grafo.agregar_arista('EA1', 'EA2')
mi_grafo.agregar_arista('EA2', 'EA3')
mi_grafo.agregar_arista('EA3', 'ALBORADA')
mi_grafo.agregar_arista('ALBORADA', 'AP1')#3PARADAS
mi_grafo.agregar_arista('AP1', 'AP2')
mi_grafo.agregar_arista('AP2', 'AP3')
mi_grafo.agregar_arista('AP3', 'PUERTO RICO')
mi_grafo.agregar_arista('PUERTO RICO', 'PUENTE DEL DIABLO')
mi_grafo.agregar_arista('PUENTE DEL DIABLO', 'PM1')#1PARADA
mi_grafo.agregar_arista('PM1', 'MAHUIXTLAN')
mi_grafo.agregar_arista('MAHUIXTLAN', 'ME1')#1PARADA
mi_grafo.agregar_arista('ME1', 'EL GRANDE')
mi_grafo.agregar_arista('EL GRANDE', 'CASAS GEO')#
mi_grafo.agregar_arista('CASAS GEO', 'CM1')#3PARADAS
mi_grafo.agregar_arista('CM1', 'CM2')
mi_grafo.agregar_arista('CM2', 'CM3')
mi_grafo.agregar_arista('CM3', 'MUNDO NUEVO')
mi_grafo.agregar_arista('LA COCA', 'MC1')#1PARADA
mi_grafo.agregar_arista('MC1', 'MUNDO NUEVO')
mi_grafo.agregar_arista('EL GRANDE', 'EC1')#2PARADAS
mi_grafo.agregar_arista('EC1', 'EC2')
mi_grafo.agregar_arista('EC2', 'LA COCA')
mi_grafo.agregar_arista('LA COCA', 'CC1')#5PARADAS
mi_grafo.agregar_arista('CC1', 'CC2')
mi_grafo.agregar_arista('CC2', 'CC3')
mi_grafo.agregar_arista('CC3', 'CC4')
mi_grafo.agregar_arista('CC4', 'CC5')
mi_grafo.agregar_arista('CC5', 'COATEPEC')
#coatepec a plaza americas por sauces
mi_grafo.agregar_arista('ZONA UV', 'ZR1')#1parada
mi_grafo.agregar_arista('ZR1', 'REBSAMEN')#1parada
mi_grafo.agregar_arista('REBSAMEN', 'RX1')#3paradas
mi_grafo.agregar_arista('RX1', 'RX2')
mi_grafo.agregar_arista('RX2', 'RX3')
mi_grafo.agregar_arista('RX3', 'XALAPA 2000')
mi_grafo.agregar_arista('XALAPA 2000', 'XA1')#6paradas
mi_grafo.agregar_arista('XA1', 'XA2')
mi_grafo.agregar_arista('XA2', 'XA3')
mi_grafo.agregar_arista('XA3', 'XA4')
mi_grafo.agregar_arista('XA4', 'XA5')
mi_grafo.agregar_arista('XA5', 'XA6')
mi_grafo.agregar_arista('XA6', 'ARCO SUR')
mi_grafo.agregar_arista('ARCO SUR', 'TEA1')#1parada
mi_grafo.agregar_arista('TEA1', 'TECNOLOGICO')
mi_grafo.agregar_arista('TECNOLOGICO', 'TA1')
mi_grafo.agregar_arista('TA1', 'TA2')
mi_grafo.agregar_arista('TA2', 'TA3')
mi_grafo.agregar_arista('TA3', 'TA4')
mi_grafo.agregar_arista('TA4', 'PLAZA AMERICAS')
#DONDE SE COMIENZA
mi_grafo.agregar_arista('SAUCES', 'COATEPEC')#10paradas
mi_grafo.agregar_arista('SAUCES', 'SZ1')#7paradas
mi_grafo.agregar_arista('SZ1', 'SZ2')
mi_grafo.agregar_arista('SZ2', 'SZ3')
mi_grafo.agregar_arista('SZ3', 'SZ4')
mi_grafo.agregar_arista('SZ4', 'SZ5')
mi_grafo.agregar_arista('SZ5', 'SZ6')
mi_grafo.agregar_arista('SZ6', 'SZ7')
mi_grafo.agregar_arista('SZ7', 'ZONA UV')
"""despues de coatepec
mi_grafo.agregar_arista('COATEPEC', 'SAN MARCOS')
mi_grafo.agregar_arista('SAN MARCOS', 'XICO')
mi_grafo.agregar_arista('XICO', 'TEOCELO')
"""
mi_grafo.mostrar_grafo()
#mi_grafo.dibujar_grafo()
mi_grafo.dibujar_grafo()