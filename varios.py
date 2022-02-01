def getAptitud(listaBeneficio:list,listaGarrafones:list,individuo,enviarTodo):
    cargaMaximaGarrafones = 72
    listaPedidosPosibles = []
    aptitudBase = 0
    garrafonesActuales = 0
    for i in range(len(individuo)):
        garrafonesActuales += listaGarrafones[individuo[i]]
        if(garrafonesActuales<=cargaMaximaGarrafones):
            listaPedidosPosibles.append(individuo[i])
            aptitudBase += listaBeneficio[individuo[i]]
        else:
            garrafonesActuales-=listaGarrafones[individuo[i]]
            break
    aptitudReal = len(listaPedidosPosibles)*aptitudBase
    # print(f"mi aptitud es {aptitudReal}")
    # print(f"mis pedidos {listaPedidosPosibles}")
    if(enviarTodo):
        return listaPedidosPosibles,aptitudReal
    else:
        return aptitudReal


    
