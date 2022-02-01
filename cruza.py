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
        padre = parejas[0][0]
        madre = parejas[0][1]
        hijos = pmx(padre,madre)
        listaHijos.append(hijos[0])
        listaHijos.append(hijos[1])
     
    return listaHijos



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



