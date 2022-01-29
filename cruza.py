import  random
from ssl import PEM_cert_to_DER_cert



def generarCruza(listasPedidos:list):
    listaPedidosAuxiliar = listasPedidos.copy()
    listaHijos = []
    listaParejas = []
    while ( len(listasPedidos) > 0 ):
        tuplaPareja = []
        individuo1 = random.choice(listasPedidos)
        listasPedidos.remove(individuo1)
        # print(f"este es el individuo1",individuo1)
        # print(f"estas es la lista de pedidos despuse de remover {listasPedidos}")
        if(len(listasPedidos)==0):
            individuo2 = random.choice(listaPedidosAuxiliar)
            # print(f"este es el individuo2",individuo2)
        else:
            individuo2 = random.choice(listasPedidos)
            listasPedidos.remove(individuo2)
            # print(f"este es el individuo2",individuo2)
            # print(f"estas es la lista de pedidos despuse de remover {listasPedidos}")
        tuplaPareja.append([individuo1,individuo2])
        listaParejas.append(tuplaPareja)

    
    
    for parejas in listaParejas:
        # print("esta es la pareja",parejas)
        seleccionCruza = [random.randint(0, len(listaPedidosAuxiliar[0])-1),random.randint(0, len(listaPedidosAuxiliar[0])-1),random.randint(0, len(listaPedidosAuxiliar[0])-1)]
        seleccionCruza.sort()
        seleccionCruza1 = seleccionCruza[0]
        seleccionCruza2 = seleccionCruza[1]
        seleccionCruza3 = seleccionCruza[2]
        padre = parejas[0][0]
        madre = parejas[0][1]
        hijos = pmx(padre,madre)
        listaHijos.append(hijos[0])
        listaHijos.append(hijos[1])
     
    return listaHijos


        


def cruza(corte1,corte2,corte3,padre,madre):
    # print(f"padre {padre}")
    # print(f"madre {madre}")
    # print(f"cortes {corte1} {corte2} {corte3}")

    listaCompletos = padre.copy()
    listaCompletos.sort()
    listaFaltantesHijo1 = []
    listaFaltantesHijo2 = []
    listaRepetidosHijo1 = []
    listaRepetidosHijo2 = []

    hijo1 = []
    hijo2 = []
    for index in range(len(padre)):
        if index < corte1:
            hijo1.append(padre[index])
            hijo2.append(madre[index])
        else:
            hijo1.append(madre[index])
            hijo2.append(padre[index])
    
    for i in range(len(listaCompletos)):
        if(hijo1.count(listaCompletos[i])>1):
            listaRepetidosHijo1.append(listaCompletos[i]) 
        
        if(hijo1.count(listaCompletos[i])==0):
            listaFaltantesHijo1.append(listaCompletos[i])

        if(hijo2.count(listaCompletos[i])>1):
            listaRepetidosHijo2.append(listaCompletos[i]) 
        
        if(hijo2.count(listaCompletos[i])==0):
            listaFaltantesHijo2.append(listaCompletos[i])

    # print(f"len de repetidos hijo1 {len(listaFaltantesHijo1)}")
    # print(f"len de repetidos hijo2 {len(listaFaltantesHijo2)}")

    for i in range(len(listaRepetidosHijo1)):
        indexCambio = hijo1.index(listaRepetidosHijo1[i])
        valorCambio = random.choice(listaFaltantesHijo1)
        listaFaltantesHijo1.remove(valorCambio)
        hijo1[indexCambio] = valorCambio

    for i in range(len(listaRepetidosHijo2)):
        indexCambio = hijo2.index(listaRepetidosHijo2[i])
        valorCambio = random.choice(listaFaltantesHijo2)
        listaFaltantesHijo2.remove(valorCambio)
        hijo2[indexCambio] = valorCambio

    return hijo1, hijo2


def _repeated(element, collection):
    c = 0
    for e in collection:
        if e == element:
            c += 1
    return c > 1
 
def _swap(data_a, data_b, cross_points):
    c1, c2 = cross_points
    new_a = data_a[:c1] + data_b[c1:c2] + data_a[c2:]
    new_b = data_b[:c1] + data_a[c1:c2] + data_b[c2:]
    return new_a, new_b
 
 
def _map(swapped, cross_points):
    n = len(swapped[0])
    c1, c2 = cross_points
    s1, s2 = swapped
    map_ = s1[c1:c2], s2[c1:c2]
    for i_chromosome in range(n):
        if not c1 < i_chromosome < c2:
            for i_son in range(2):
                while _repeated(swapped[i_son][i_chromosome], swapped[i_son]):
                    map_index = map_[i_son].index(swapped[i_son][i_chromosome])
                    swapped[i_son][i_chromosome] = map_[1-i_son][map_index]
    return s1, s2
 
 
def pmx(parent_a, parent_b):
    assert(len(parent_a) == len(parent_b))
    n = len(parent_a)
    cross_points = sorted([random.randint(0, n) for _ in range(2)])
    swapped = _swap(parent_a, parent_b, cross_points)
    mapped = _map(swapped, cross_points)
 
    return mapped



