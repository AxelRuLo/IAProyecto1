import random

pmi = 0.2
pmg = 0.4


def mutacion(listaHijos):
    global pmi
    global pmg
        
    for index in range(len(listaHijos)):
        pmiActual = random.random()
        if pmiActual <= pmi:
            for bit in range(len(listaHijos[index])):
                pmgActual = random.random()
                if pmgActual <= pmg:
                    espacioMutar = random.randint(0,len(listaHijos[index]))-1 
                    valorMutar = listaHijos[index][bit]
                    valorCambiar = listaHijos[index][espacioMutar]
                    listaHijos[index][bit] = valorCambiar
                    listaHijos[index][espacioMutar] = valorMutar
    return listaHijos
