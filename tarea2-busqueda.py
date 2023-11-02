# CC5213 - TAREA 2
# 28 de septiembre de 2023
# Alumno: [nombre]

import sys
import os.path
import pickle
import numpy as np
import scipy

import aux_func


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

    # se crea una lista con todos las ventanas de las canciones R juntas
    ventanas_R_full = []

    # para cada lista de ventanas de la primera canción
    for ventanas in ventanas_R:
        # para cada ventana de la canción
        for ventana in ventanas:
            # se añade a la lista de ventanas
            ventanas_R_full.append(ventana)

    # se crea un array con todos los descriptores de las ventanas de las canciones en R juntas (en el mismo orden que las ventanas)
    descriptores_R_full = []

    # para cada lista de de descriptores
    for descriptor in descriptores_R:
        if len(descriptores_R_full) == 0:
            descriptores_R_full = descriptor
        else:
            descriptores_R_full = np.vstack([descriptores_R_full, descriptor])

    print("TAMAÑO DE LA LISTA DE VENTANAS R",len(ventanas_R_full))

    print("TAMAÑO DEl VECTOR DE DESCRIPTORES R",descriptores_R_full.shape)


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
