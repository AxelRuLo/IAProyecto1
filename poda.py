from varios import getAptitud


def podaMejoresIndividuos(listaBeneficio:list,listaGarrafones:list,listaIndividuos:list):
    listaMejoresIndividuos = []
    listaAptitud = []

    for index in range(len(listaIndividuos)):
        listaAptitud.append(getAptitud(listaBeneficio,listaGarrafones,listaIndividuos[index],False))
    
    if(len(listaIndividuos)<10):
        return listaIndividuos
    else:
        for i in range(10):
            valorMaximo = max(listaAptitud)
            indexMaximo =listaAptitud.index(valorMaximo)
            listaMejoresIndividuos.append(listaIndividuos[indexMaximo])
            listaAptitud.pop(indexMaximo)
            listaIndividuos.pop(indexMaximo)
        return listaMejoresIndividuos

    

