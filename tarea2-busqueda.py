# CC5213 - TAREA 2
# 28 de septiembre de 2023
# Alumno: [nombre]

import sys
import os.path
import pickle
import numpy as np


def tarea2_busqueda(dir_descriptores_q, dir_descriptores_r, dir_resultados_knn):
    if not os.path.isdir(dir_descriptores_q):
        print("ERROR: no existe directorio {}".format(dir_descriptores_q))
        sys.exit(1)
    elif not os.path.isdir(dir_descriptores_r):
        print("ERROR: no existe directorio {}".format(dir_descriptores_r))
        sys.exit(1)
    elif os.path.exists(dir_resultados_knn):
        print("ERROR: ya existe archivo {}".format(dir_resultados_knn))
        sys.exit(1)

    # se obtienen los descriptores y ventanas de Q
    # lista para los descriptores
    descriptores_Q = []    
    # lista para las ventanas
    ventanas_Q = []

    # para cada archivo en el directorio de descriptores q (wav, .npy o pickle)
    for descriptores in os.listdir(dir_descriptores_q):
        # si es un archivo .npy, es el descriptor
        if(".npy" in descriptores):
            # se pasa a un objeto ndp.dArray
            d = np.load(dir_descriptores_q+"/"+descriptores)
            # se guarda en la lista de descriptores
            descriptores_Q.append(d)
        # si es un archivo .pickle, es una lista de ventanas
        if(".pickle" in descriptores):
            # se pasa a un objeto list 
            with open(dir_descriptores_q+"/"+descriptores, "rb") as file:
                l_w: list = pickle.load(file)
                # y se añade a las lista de ventanas Q
                ventanas_Q.append(l_w)


    # se obtienen los descriptores y ventanas de R
    # lista para los descriptores
    descriptores_R = []    
    # lista para las ventanas
    ventanas_R = []

    # para cada archivo en el directorio de descriptores q (wav, .npy o pickle)
    for descriptores in os.listdir(dir_descriptores_r):
        # si es un archivo .npy, es el descriptor
        if(".npy" in descriptores):
            # se pasa a un objeto ndp.dArray
            d = np.load(dir_descriptores_r+"/"+descriptores)
            # se guarda en la lista de descriptores
            descriptores_R.append(d)
        # si es un archivo .pickle, es una lista de ventanas
        if(".pickle" in descriptores):
            # se pasa a un objeto list 
            with open(dir_descriptores_r+"/"+descriptores, "rb") as file:
                l_w: list = pickle.load(file)
                # y se añade a las lista de ventanas Q
                ventanas_R.append(l_w)



    #  3-para cada descriptor q localizar el mas cercano en R
    #     usar cdist o usar indices de busqueda eficiente
    #  3-crear dir_resultados_knn
    #    os.makedirs(dir_resultados_knn, exist_ok=True)
    #  4-escribir los knn en dir_resultados_knn
    #    incluir tambien los tiempos que representa cada ventana de q y r
    # borrar la siguiente linea
    print("ERROR: no implementado!")


# inicio de la tarea
if len(sys.argv) < 4:
    print("Uso: {} [dir_descriptores_q] [dir_descriptores_r] [dir_resultados_knn]".format(sys.argv[0]))
    sys.exit(1)

dir_descriptores_q = sys.argv[1]
dir_descriptores_r = sys.argv[2]
dir_resultados_knn = sys.argv[3]

tarea2_busqueda(dir_descriptores_q, dir_descriptores_r, dir_resultados_knn)
