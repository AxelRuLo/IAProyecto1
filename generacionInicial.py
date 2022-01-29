import random

from cruza import generarCruza


def generarPedidos():
    listaPedidos = []
    listaNumerosGarrafones = []
    listaBeneficio = []
    listaUbicacion = []
    numeroPedidosGenerar  = random.randint(1,20)
    for i in range(numeroPedidosGenerar):
        listaPedidos.append(f"P{i}")
        listaNumerosGarrafones.append(random.randint(1,100))
        # pendiente beneficio y ubicacion
    # print(listaPedidos)
    # print(listaNumerosGarrafones)
    listaPedidosRevuelta = random.sample(listaPedidos, len(listaPedidos))

    return [listaPedidos, listaPedidosRevuelta],[listaNumerosGarrafones]

def generacionBeneficio(listaPedidos:list):
    pass

def generacionUbicacion(listaPedidos:list):
    pass





pedidos,garrafones = generarPedidos()

for i in range(5):
    hijos = generarCruza(pedidos.copy())
    combinados = hijos + pedidos.copy()
    pedidos = combinados

for i in pedidos:
    print(i)