
import math
import dijkstra

mapa = [
        [(16.752933, -93.124238),(16.752805, -93.123354),(16.752680, -93.122455),(16.752569, -93.121590),(16.752458, -93.120723),(16.752337, -93.119911),(16.752230, -93.119105),(16.752115, -93.118260)],
        [(16.752100, -93.124360),(16.752005, -93.123509),(16.751865, -93.122589),(16.751745, -93.121745),(16.751623, -93.120901),(16.751510, -93.120070),(16.751394, -93.119238),(16.751278, -93.118404)],
        [(16.751255, -93.124521),(16.751139, -93.123628),(16.751023, -93.122734),(16.750900, -93.121897),(16.750800, -93.121058),(16.750696, -93.120223),(16.750575, -93.119370),(16.750470, -93.118539)],
        [(16.750470, -93.124651),(16.750344, -93.123764),(16.750235, -93.122865),(16.750120, -93.122015),(16.749989, -93.121180),(16.749881, -93.120373),(16.749773, -93.119504),(16.749668, -93.118650)],
        [(16.749688, -93.124804),(16.749562, -93.123897),(16.749426, -93.122985),(16.749320, -93.122175),(16.749202, -93.121330),(16.749078, -93.120557),(16.748957, -93.119655),(16.748846, -93.118810)],
        [(16.748952, -93.124914),(16.748824, -93.124040),(16.748670, -93.123109),(16.748558, -93.122321),(16.748430, -93.121466),(16.748300, -93.120695),(16.748160, -93.119792),(16.748019, -93.118961)],
        [(16.748174, -93.125065),(16.748018, -93.124142),(16.747866, -93.123238),(16.747758, -93.122466),(16.747618, -93.121631),(16.747491, -93.120845),(16.747355, -93.119925),(16.747219, -93.119107)],
        [(16.747410, -93.125241),(16.747245, -93.124287),(16.747091, -93.123365),(16.746981, -93.122598),(16.746830, -93.121750),(16.746705, -93.120994),(16.746557, -93.120073),(16.746433, -93.119284)],
       ]

mapa_lineas = [
        (16.752933, -93.124238),(16.752805, -93.123354),(16.752680, -93.122455),(16.752569, -93.121590),(16.752458, -93.120723),(16.752337, -93.119911),(16.752230, -93.119105),(16.752115, -93.118260),
        (16.752100, -93.124360),(16.752005, -93.123509),(16.751865, -93.122589),(16.751745, -93.121745),(16.751623, -93.120901),(16.751510, -93.120070),(16.751394, -93.119238),(16.751278, -93.118404),
        (16.751255, -93.124521),(16.751139, -93.123628),(16.751023, -93.122734),(16.750900, -93.121897),(16.750800, -93.121058),(16.750696, -93.120223),(16.750575, -93.119370),(16.750470, -93.118539),
        (16.750470, -93.124651),(16.750344, -93.123764),(16.750235, -93.122865),(16.750120, -93.122015),(16.749989, -93.121180),(16.749881, -93.120373),(16.749773, -93.119504),(16.749668, -93.118650),
        (16.749688, -93.124804),(16.749562, -93.123897),(16.749426, -93.122985),(16.749320, -93.122175),(16.749202, -93.121330),(16.749078, -93.120557),(16.748957, -93.119655),(16.748846, -93.118810),
        (16.748952, -93.124914),(16.748824, -93.124040),(16.748670, -93.123109),(16.748558, -93.122321),(16.748430, -93.121466),(16.748300, -93.120695),(16.748160, -93.119792),(16.748019, -93.118961),
        (16.748174, -93.125065),(16.748018, -93.124142),(16.747866, -93.123238),(16.747758, -93.122466),(16.747618, -93.121631),(16.747491, -93.120845),(16.747355, -93.119925),(16.747219, -93.119107),
        (16.747410, -93.125241),(16.747245, -93.124287),(16.747091, -93.123365),(16.746981, -93.122598),(16.746830, -93.121750),(16.746705, -93.120994),(16.746557, -93.120073),(16.746433, -93.119284),
       ]

recorridos =[]

recorridos_nodos =[]

recorrido_extenso = []


def puntoCercano(x1,y1):
        listaPuntos = []
        listaDistancias = []
        for calle in range(len(mapa)):
                for cord in range(len(mapa[calle])):
                        x2 = mapa[calle][cord][0]
                        y2 = mapa[calle][cord][1]
                        # Formula de haversine
                        parte1 = math.acos(math.cos(math.radians(90-x1))*math.cos(math.radians(90-x2)) +
                                 math.sin(math.radians(90-x1))*math.sin(math.radians(90-x2))*math.cos(math.radians(y1-y2)))
                        formula = round(6371 * parte1 *1000,3)
                        listaDistancias.append(formula)
                        listaPuntos.append([mapa[calle][cord],formula])
        punto = listaDistancias.index(min(listaDistancias))
        listaPuntos[punto].append(punto)
        return listaPuntos[punto]
        

def recorrido(nodoInicial,listUbicaciones):
        
        print("--------------------------------------------")
        listaRecorrido = []
        listaCordenadas = []
        
        listaRecorrido.append(nodoInicial)
        listaCordenadas.append(mapa_lineas[nodoInicial])
        nodo = nodoInicial
        
        for i in range(len(listUbicaciones.copy())):
                listDistancia = []
                for i in listUbicaciones:
                        listDistancia.append(dijkstra.find_shortest_distance(nodo,i[2]))
                index = listDistancia.index(min(listDistancia))
                nodo = listUbicaciones[index][2]
                listaRecorrido.append(nodo)
                listaCordenadas.append(listUbicaciones[index][0])
                listUbicaciones.pop(index)
        listaRecorrido.append(nodoInicial)
        listaCordenadas.append(mapa_lineas[nodoInicial])


        recorridos.append(listaCordenadas.copy()) 
        print(listaRecorrido)
        # listaRecorrido.sort()
        recorridos_nodos.append(listaRecorrido.copy())
        
        # print(listaCordenadas)
        recorridoExtenso(listaRecorrido.copy())
        print("--------------------------------------------")
        
def recorridoExtenso(listNodos):
        global recorrido_extenso
        recorrido_ruta_nodo= []
        recorrido_ruta_cord= []
        
        print("--------------------------------------------")
        for i in range(len(listNodos)):
                if(i<len(listNodos)-1):
                        aux =dijkstra.find_shortest_path(listNodos[i],listNodos[i+1])
                        # aux.pop()
                        recorrido_ruta_nodo.append(aux.copy())
                else:
                        recorrido_ruta_nodo[len(recorrido_ruta_nodo)-1].append(listNodos[0])
        for lista in recorrido_ruta_nodo:
                aux = []
                for nodo in lista:
                        aux.append(mapa_lineas[nodo])        
                recorrido_ruta_cord.append(aux.copy())
        recorrido_extenso.append(recorrido_ruta_cord.copy())
        
        
        print("--------------------------------------------")
                

def cleanRutas():
        global recorridos,recorridos_nodos,recorrido_extenso
        recorridos.clear()
        recorridos_nodos.clear()
        recorrido_extenso.clear()              
# print(puntoCercano(16.748917, -93.122969))
