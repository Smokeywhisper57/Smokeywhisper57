from graforecorridos import *
# Definición de los nodos
a, b, c, d, e, f, g, h = "SAUCES", "b", "c", "d", "e", "f", "g", "h"
# Crear el grafo
grafo = Grafo()
#coatepec-sauces
agregar(grafo,"SAUCES")
    #paradas
agregar(grafo,"SC1")#calle bolivia
agregar(grafo,"SC2")#fasti
agregar(grafo,"SC3")#circuitos presidentes
agregar(grafo,"SC4")#DIF
agregar(grafo,"SC5")#Autohotel
agregar(grafo,"SC5")#arenales
agregar(grafo,"SC6")#parque pequeño
agregar(grafo,"SC7")#desviacion a pacho
agregar(grafo,"SC8")#plaza orquideas
agregar(grafo,"SC9")#entrada coatepec
agregar(grafo,"SC10")#parada intermedia
agregar(grafo,"COATEPEC")
#coatepec a Americas---------------------------------------------------------------------------------------------------------------------
    #coatepec-la coca
#coatepec
agregar(grafo,"CC1")#dif
agregar(grafo,"CC2")#fasti
agregar(grafo,"CC3")
agregar(grafo,"CC4")
agregar(grafo,"CC5")
agregar(grafo,"LA COCA")
    #lacoca-mundo nuevo
#la coca
agregar(grafo,"MC1")
agregar(grafo,"MUNDO NUEVO")
    #Mundo nuevo-casasgeo
#Mundo nuevo
agregar(grafo,"CM1")
agregar(grafo,"CM2")
agregar(grafo,"CM3")
agregar(grafo,"CASAS GEO")
    #lacoca-elgrande
#lacoca
agregar(grafo,"EC1")
agregar(grafo,"EC2")
agregar(grafo,"EL GRANDE")
    #elgrande-mahuixtlan
#elgrande
agregar(grafo,"ME1")
agregar(grafo,"MAHUIXTLAN")
    #mahuixtlan-puerto rico
#mahuixtlan
agregar(grafo,"PM1")
agregar(grafo,"PUENTE DEL DIABLO")
agregar(grafo,"PUERTO RICO")
    #puerto rico-alborada
#puerto rico
agregar(grafo,"AP1")
agregar(grafo,"AP2")
agregar(grafo,"AP3")
agregar(grafo,"ALBORADA")
    #alborada-estanzuela
#alborada
agregar(grafo,"EA1")
agregar(grafo,"EA2")
agregar(grafo,"EA3")
agregar(grafo,"ESTANZUELA")
    #esttanzuela-las trancas
#estanzuela
agregar(grafo,"TE1")
agregar(grafo,"TE2")
agregar(grafo,"TE3")
agregar(grafo,"TE4")
agregar(grafo,"TE5")
agregar(grafo,"TE6")
agregar(grafo,"TE7")
agregar(grafo,"LAS TRANCAS")
    #las trancas-americas
#las trancas
agregar(grafo,"TRA1")
agregar(grafo,"PLAZA AMERICAS")
#sauces a plaza americas---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #sauces-zonauv
#sauces
agregar(grafo,"SZ1")
agregar(grafo,"SZ2")
agregar(grafo,"SZ3")
agregar(grafo,"SZ4")
agregar(grafo,"SZ5")
agregar(grafo,"SZ6")
agregar(grafo,"SZ7")
agregar(grafo,"ZONA UV")
    #zonauv-rebsamen
#zonauv
agregar(grafo,"ZR1")
agregar(grafo,"REBSAMEN")
    #rebsamen-xalapa2000
#rebsamen
agregar(grafo,"RX1")
agregar(grafo,"RX2")
agregar(grafo,"RX3")
agregar(grafo,"XALAPA 2000")
    #xalapa2000-arcosur
agregar(grafo,"XA1")
agregar(grafo,"XA2")
agregar(grafo,"XA3")
agregar(grafo,"XA4")
agregar(grafo,"XA5")
agregar(grafo,"XA6")
agregar(grafo,"ARCO SUR")
    #arcosur-tecnologico
agregar(grafo,"TEA1")
agregar(grafo,"AT2")
agregar(grafo,"AT3")
agregar(grafo,"AT4")
agregar(grafo,"TECNOLOGICO")
    #tecnologico a plaza americas
agregar(grafo,"TA1")
agregar(grafo,"TA2")
agregar(grafo,"TA3")
agregar(grafo,"TA4")


#verde
agregar(grafo,"PLAZA CRISTAL")
agregar(grafo,"URBAN CENTER")
agregar(grafo,"CENTRO")
agregar(grafo,"PLAZA ANIMAS")
agregar(grafo,"TESORERIA")
#mas afuera de coatepec
agregar(grafo,"XICO")
agregar(grafo,"TEOCELO")
agregar(grafo,"SAN MARCOS")
#ruta verde
agregar(grafo,"CBTIS13")
agregar(grafo,"SAMS")
agregar(grafo,"RUIZ CORTINES")
agregar(grafo,"URBAN CENTER")
agregar(grafo,"IMSS")
agregar(grafo,"PLAZA ANIMAS")
agregar(grafo,"ARAUCARIAS")
#fovisste
agregar(grafo,"CENTRO")
"""fovisste
relacionar(grafo,"ARAUCARIAS" , "CENTRO")
relacionar(grafo,"SAUCES" , "CENTRO")
#relacionar(grafo,"ARAUCARIAS" , "SAMS")
relacionar(grafo,"PLAZA ANIMAS" , "PLAZA AMERCIAS")
verde
relacionar(grafo,"ARAUCARIAS" , "PLAZA CRISTAL")
relacionar(grafo,"RUIZ CORTINES" , "TESORERIA")
relacionar(grafo,"URBAN CENTER" , "TESORERIA")
relacionar(grafo,"RUIZ CORTINES" , "IMSS")
relacionar(grafo,"SAUCES" , "IMSS")
relacionar(grafo,"PLAZA CRISTAL" , "URBAN CENTER")
relacionar(grafo,"PLAZA AMERICAS" , "SAMS")
relacionar(grafo,"ARAUCARIAS" , "SAMS")
"""
#plaza americas a coatepec
relacionar(grafo,"PLAZA AMERICAS" , "TRA1",1)#1PARADA
relacionar(grafo,"TRA1" , "LAS TRANCAS",1)
relacionar(grafo,"LAS TRANCAS" , "TE1",1)#7PARADAS
relacionar(grafo,"TE1" , "TE2",1)
relacionar(grafo,"TE2" , "TE3",1)
relacionar(grafo,"TE3" , "TE4",1)
relacionar(grafo,"TE4" , "TE5",1)
relacionar(grafo,"TE5" , "TE6",1)
relacionar(grafo,"TE6" , "TE7",1)
relacionar(grafo,"TE7" , "ESTANZUELA",1)#
relacionar(grafo,"ESTANZUELA" , "EA1",1)#3PARADAS
relacionar(grafo,"EA1" , "EA2",1)
relacionar(grafo,"EA2" , "EA3",1)
relacionar(grafo,"EA3" , "ALBORADA",1)
relacionar(grafo,"ALBORADA" , "AP1",1)#3PARADAS
relacionar(grafo,"AP1" , "AP2",1)
relacionar(grafo,"AP2" , "AP3",1)
relacionar(grafo,"AP3" , "PUERTO RICO",1)
relacionar(grafo,"PUERTO RICO" , "PUENTE DEL DIABLO",1)
relacionar(grafo,"PUENTE DEL DIABLO" , "PM1",1)#1PARADA
relacionar(grafo,"PM1" , "MAHUIXTLAN",1)
relacionar(grafo,"MAHUIXTLAN" , "ME1",1)#1PARADA
relacionar(grafo,"ME1" , "EL GRANDE",1)
relacionar(grafo,"EL GRANDE" , "CASAS GEO",1)#
relacionar(grafo,"CASAS GEO" , "CM1",1)#3PARADAS
relacionar(grafo,"CM1" , "CM2",1)
relacionar(grafo,"CM2" , "CM3",1)
relacionar(grafo,"CM3" , "MUNDO NUEVO",1)
relacionar(grafo,"LA COCA" , "MC1",1)#1PARADA
relacionar(grafo,"MC1" , "MUNDO NUEVO",1)
relacionar(grafo,"EL GRANDE" , "EC1",1)#2PARADAS
relacionar(grafo,"EC1" , "EC2",1)
relacionar(grafo,"EC2" , "LA COCA",1)
relacionar(grafo,"LA COCA" , "CC1",1)#5PARADAS
relacionar(grafo,"CC1" , "CC2",1)
relacionar(grafo,"CC2" , "CC3",1)
relacionar(grafo,"CC3" , "CC4",1)
relacionar(grafo,"CC4" , "CC5",1)
relacionar(grafo,"CC5" , "COATEPEC",1)
#coatepec a plaza americas por sauces
relacionar(grafo,"ZONA UV" , "ZR1",1)#1parada
relacionar(grafo,"ZR1" , "REBSAMEN",1)#1parada
relacionar(grafo,"REBSAMEN" , "RX1",1)#3paradas
relacionar(grafo,"RX1" , "RX2",1)
relacionar(grafo,"RX2" , "RX3",1)
relacionar(grafo,"RX3" , "XALAPA 2000",1)
relacionar(grafo,"XALAPA 2000" , "XA1",1)#6paradas
relacionar(grafo,"XA1" , "XA2",1)
relacionar(grafo,"XA2" , "XA3",1)
relacionar(grafo,"XA3" , "XA4",1)
relacionar(grafo,"XA4" , "XA5",1)
relacionar(grafo,"XA5" , "XA6",1)
relacionar(grafo,"XA6" , "ARCO SUR",1)
relacionar(grafo,"ARCO SUR" , "TEA1",1)#1parada
relacionar(grafo,"TEA1" , "TECNOLOGICO",1)
relacionar(grafo,"TECNOLOGICO" , "TA1",1)
relacionar(grafo,"TA1" , "TA2",1)
relacionar(grafo,"TA2" , "TA3",1)
relacionar(grafo,"TA3" , "TA4",1)
relacionar(grafo,"TA4" , "PLAZA AMERICAS",1)
#DONDE SE COMIENZA
relacionar(grafo,"SAUCES" , "COATEPEC",1)#10paradas
relacionar(grafo,"SAUCES" , "SZ1",1)#7paradas
relacionar(grafo,"SZ1" , "SZ2",1)
relacionar(grafo,"SZ2" , "SZ3",1)
relacionar(grafo,"SZ3" , "SZ4",1)
relacionar(grafo,"SZ4" , "SZ5",1)
relacionar(grafo,"SZ5" , "SZ6",1)
relacionar(grafo,"SZ6" , "SZ7",1)
relacionar(grafo,"SZ7" , "ZONA UV",1)
"""despues de coatepec
relacionar(grafo,"COATEPEC" , "SAN MARCOS")
relacionar(grafo,"SAN MARCOS" , "XICO")
relacionar(grafo,"XICO" , "TEOCELO")
"""


print(caminoMinimo(grafo, "ZONA UV","SAUCES"))
grafo.dibujar_grafo()