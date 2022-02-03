import random
from cruza import generarCruza
import dijkstra
from mapa import puntoCercano, recorrido
from mutacion import mutacion
from poda import podaMejoresIndividuos
from varios import getAptitud

nodoSucursal = 63

pedidos_table = []

def generarPedidos():
    listaPedidos = []
    listaNumerosGarrafones = []
    listaBeneficio = []
    listaUbicacion = []
    numeroPedidosGenerar  = random.randint(1,20)
    for i in range(numeroPedidosGenerar):
        listaPedidos.append(i)
        listaNumerosGarrafones.append(random.randint(1,30))
        listaUbicacion.append(generacionUbicacion())
    listaBeneficio = generacionBeneficio(listaUbicacion,listaNumerosGarrafones)
        # pendiente beneficio y ubicacion
    # print(listaPedidos)
    # print(listaNumerosGarrafones)
    listaPedidosRevuelta = random.sample(listaPedidos, len(listaPedidos))

    return [listaPedidos, listaPedidosRevuelta],listaNumerosGarrafones,listaUbicacion,listaBeneficio

def generacionBeneficio(listasUbicacion:list,listaGarrafones:list):
    global nodoSucursal
    listaBeneficio = []
    for i in range(len(listasUbicacion)):
        distanciaARecorrer = dijkstra.find_shortest_distance(nodoSucursal,listasUbicacion[i][2])
        cuantoNosCuestaEntregar = (distanciaARecorrer/1000)*10 
        cuantoGanaremos = listaGarrafones[i]*7
        beneficio = cuantoGanaremos-cuantoNosCuestaEntregar
        listaBeneficio.append(beneficio)
    return listaBeneficio


def generacionUbicacion():
    mapa = [[16.752933, -93.124238],[16.752805, -93.123354],[16.752680, -93.122455],[16.752569, -93.121590],[16.752569, -93.121590],[16.752337, -93.119911],[16.752230, -93.119105],[16.752230, -93.119105],[16.752100, -93.124360],[16.751865, -93.122589],[16.751865, -93.122589],[16.751745, -93.121745],[16.751510, -93.120070],[16.751510, -93.120070],[16.751394, -93.119238],[16.751278, -93.118404],[16.749668, -93.118650],[16.751139, -93.123628],[16.751023, -93.122734],[16.750900, -93.121897],[16.750800, -93.121058],[16.750696, -93.120223],[16.750696, -93.120223],[16.750470, -93.118539],[16.750470, -93.124651],[16.750344, -93.123764],[16.750235, -93.122865],[16.750120, -93.122015],[16.750120, -93.122015],[16.749881, -93.120373],[16.749773, -93.119504],[16.749668, -93.118650],[16.749688, -93.124804],[16.749562, -93.123897],[16.749426, -93.122985],[16.749320, -93.122175],[16.749202, -93.121330],[16.749071, -93.120550],[16.749071, -93.120550],[16.748846, -93.118810],[16.748952, -93.124914],[16.748824, -93.124040],[16.748670, -93.123109],[16.748558, -93.122321],[16.748430, -93.121466],[16.748300, -93.120695],[16.748160, -93.119792],[16.748019, -93.118961],[16.748174, -93.125065],[16.748018, -93.124142],[16.747866, -93.123238],[16.747758, -93.122466],[16.747618, -93.121631],[16.747491, -93.120845],[16.747355, -93.119925],[16.747219, -93.119107],[16.747410, -93.125241],[16.747245, -93.124287],[16.747091, -93.123365],[16.746981, -93.122598],[16.746830, -93.121750],[16.746705, -93.120994],[16.746557, -93.120073],[16.746433, -93.119284]]
    puntoRandom = random.choice(mapa)
    infomracionGeneralUbicacion = puntoCercano(puntoRandom[0]+.000001,puntoRandom[1]-.0000001)

    # print("\n")
    # print(puntoRandom)
    # print(infomracionGeneralUbicacion)
    return infomracionGeneralUbicacion


def algoritmogenetico():
    pedidos,garrafones,ubicacion,beneficio = generarPedidos()
    tablePedidos(pedidos.copy(),garrafones.copy(),ubicacion.copy(),beneficio.copy())
    numeroPedidos = len(pedidos[0])
    print(pedidos)
    print(garrafones)

    while numeroPedidos>0:
        print("\n INICIA VUELTA")
        for i in range(100):
            hijos = generarCruza(pedidos.copy())
            hijos = mutacion(hijos.copy())
            combinados = hijos + pedidos.copy()
            pedidos = combinados
            pedidos = podaMejoresIndividuos(beneficio,garrafones,pedidos)


        listaMejoresPedidos = []
        for i in pedidos:
            listaMejoresPedidos.append(getAptitud(beneficio,garrafones,i,False))

        valorMaximo = max(listaMejoresPedidos)
        indexMejor = listaMejoresPedidos.index(valorMaximo)

        mejorAptitudIndividuo = getAptitud(beneficio,garrafones,pedidos[indexMejor],True)

        # print(f"mejor valor {pedidos[indexMejor]}")
        # print(f"pedidos {getAptitud(beneficio,garrafones,pedidos[indexMejor],True)}")

        # aqui obteienes la lista de los pedidiso que entran, y le sacas la ubicacion por su id

        pedidosAuxiliar = pedidos[0]
        pedidosAuxiliar.sort()
        
        ubicacionesReccorrido = []
        for i in mejorAptitudIndividuo[0]:
            # print(i)
            pedidosAuxiliar.remove(i)
            ubicacionesReccorrido.append(ubicacion[i])
            print(ubicacion[i])
        # aqui se envia la ubicacion
        recorrido(nodoSucursal,ubicacionesReccorrido.copy())

        listaPedidosAuxiliarRevuelta = random.sample(pedidosAuxiliar, len(pedidosAuxiliar))
        # print(pedidosAuxiliar,listaPedidosAuxiliarRevuelta)

        pedidos = [pedidosAuxiliar,listaPedidosAuxiliarRevuelta]
        numeroPedidos= len(pedidosAuxiliar)
    return True 
 

def tablePedidos(pedidos:list,garrafones:list,ubicacion:list,beneficio:list):
    pedidos_table.clear()
    for i in range(len(pedidos[0])):
        pedidos_table.append([f"{pedidos[0][i]+1}",f"{garrafones[i]}",f"{ubicacion[i][0]}",f"{beneficio[i]}"])
    print(pedidos_table)
    
def cleanPedidos():
    global pedidos_table
    pedidos_table = []
    return True



    

