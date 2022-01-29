import  random



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
        hijo1, hijo2 = cruza(seleccionCruza1,seleccionCruza2,seleccionCruza3, padre, madre)
        listaHijos.append(hijo1)
        listaHijos.append(hijo2)
     
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