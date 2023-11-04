# CC5213 - TAREA 2
# 28 de septiembre de 2023
# Alumno: [nombre]

import sys
import os.path
import pickle
import numpy as np
import scipy

import aux_func

def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier

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


    # se crea una lista con todos las ventanas de las canciones Q juntas
    ventanas_Q_full = []

    # para cada lista de ventanas de la primera canción
    for ventanas in ventanas_Q:
        # para cada ventana de la canción
        for ventana in ventanas:
            # se añade a la lista de ventanas
            ventanas_Q_full.append(ventana)

    # se crea un array con todos los descriptores de las ventanas de las canciones en Q juntas (en el mismo orden que las ventanas)
    descriptores_Q_full = []

    # para cada lista de de descriptores
    for descriptor in descriptores_Q:
        if len(descriptores_Q_full) == 0:
            descriptores_Q_full = descriptor
        else:
            descriptores_Q_full = np.vstack([descriptores_Q_full, descriptor])


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


    # se calcula la matriz de distancias 
    matriz_distancias = scipy.spatial.distance.cdist(descriptores_Q_full, descriptores_R_full, metric = 'euclidean')

    #obtener la posicion del más cercano por fila
    posicion_min = np.argmin(matriz_distancias, axis=1)
    minimo = np.amin(matriz_distancias, axis=1)

    # se crea la carpeta para los resultados knn
    os.makedirs(dir_resultados_knn, exist_ok=True)

    # se crea el archivo con los resultados knn
    archivo = open(dir_resultados_knn+'/'+'resultados.txt', 'w')

    # para cada query, se escribe en el archivo con los resultados
    for i in range(len(ventanas_Q_full)):
        query = ventanas_Q_full[i]
        conocido = ventanas_R_full[posicion_min[i]]
        # desfase entre los tiempos
        dist = truncate_float(conocido.segundos_desde - query.segundos_desde, 10)
        # el puntaje 
        score = truncate_float(minimo[i], 10)
        print("{}|{}|{}|{}".format(query, conocido, dist, score), file=archivo)

    archivo.close()


# inicio de la tarea
if len(sys.argv) < 4:
    print("Uso: {} [dir_descriptores_q] [dir_descriptores_r] [dir_resultados_knn]".format(sys.argv[0]))
    sys.exit(1)

dir_descriptores_q = sys.argv[1]
dir_descriptores_r = sys.argv[2]
dir_resultados_knn = sys.argv[3]

tarea2_busqueda(dir_descriptores_q, dir_descriptores_r, dir_resultados_knn)
