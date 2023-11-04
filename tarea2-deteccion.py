# CC5213 - TAREA 2
# 28 de septiembre de 2023
# Alumno: [nombre]

import sys
import os.path


def tarea2_deteccion(dir_resultados_knn, file_resultados_txt):
    if not os.path.isdir(dir_resultados_knn):
        print("ERROR: no existe directorio {}".format(dir_resultados_knn))
        sys.exit(1)
    elif os.path.exists(file_resultados_txt):
        print("ERROR: ya existe archivo {}".format(file_resultados_txt))
        sys.exit(1)

    # lista con todas las líneas
    f_lineas = None

    # se abre el archivo con las canciones y los desfaces de tiempo
    with open(dir_resultados_knn+'/'+'resultados.txt', "r") as f:
        f_lineas = f.readlines()


    # se crea el archivo con los resultados finales 
    archivo = open(file_resultados_txt, 'w+')

    # esta función recibe un item de la lista y lo divide en sus partes
    def divide_item(item):
        # se divide el resultado por el símbolo |
        resultado_lista = item.split("|")
        # se consigue la radio y su tiempo
        radio = resultado_lista[0]
        # se consigue la canción y su tiempo
        cancion = resultado_lista[1]
        # se consigue el desfase de tiempo
        desface = float(resultado_lista[2])

        # se divide la info de la radio
        radio_lista = radio.split(";")
        # radio nombre
        radio_nombre = radio_lista[0]
        # intervalo de tiempo
        radio_delta = radio_lista[1]
        # se consigue el inicio y el final
        radio_delta = radio_delta.split("-")
        # inicio
        radio_inicio = float(radio_delta[0].strip())
        # final
        radio_final = float(radio_delta[1].strip())

        # se divide la info de la canción
        cancion_lista = cancion.split(";")
        # canción nombre
        cancion_nombre = cancion_lista[0]
        # intervalo de tiempo
        cancion_delta = cancion_lista[1]
        # se consigue el inicio y el final
        cancion_delta = cancion_delta.split("-")
        # inicio
        cancion_inicio = float(cancion_delta[0].strip())
        # final
        cancion_final = float(cancion_delta[1].strip())

        # se retorna la info
        return [[radio_nombre, radio_inicio, radio_final],[cancion_nombre, cancion_inicio, cancion_final], desface]

    # se obtiene el largo de las lista con líneas
    largo_f_lineas = len(f_lineas)


    # ultimo desface
    ult_desfase = None
    # último tiempo de inicio 
    ult_t_inicio = None
    # último tiempo de final
    ult_t_final = None
    # último archivo de Q
    ult_radio = None
    # último arhcivo de R
    ult_cancion = None
    # última confianza
    ult_confianza = None
    # utlimos "strikes ocurridos"
    ult_strikes = None

    # dice si es está o no en un fragmento
    in_fragmento = False

    # indice
    i = 0

    # número de "strikes" permitidos, si es que se está en fun fragmento y el nombre es distinto strike veces, entonces ya terminó el fragmento
    strikes_permitidos = 3


    # se leen todas las líneas
    while i < largo_f_lineas:
        # se obtiene el elemento actual que se está analizando
        elem_i = f_lineas[i]
        # se obtiene como estrcutura
        elem_i_struct = divide_item(elem_i)

        # si es que no se está en un fragmento (slice) y no es el último de la lista
        if(not in_fragmento and (i != largo_f_lineas-1)):
            # se revisa si el que viene tiene el mismo nombre y desfase 
            # se obtiene el elemento siguiente
            elem_i_sgte = f_lineas[i+1]
            # se obtiene como estrcutura
            elem_i_sgte_struct = divide_item(elem_i_sgte)

            # se comparan los nombres y desfases
            nombre_i = elem_i_struct[1][0]
            desfase_i = elem_i_struct[2]
            nombre_i_sgte = elem_i_sgte_struct[1][0]
            desfase_i_sgte = elem_i_sgte_struct[2]

            if(nombre_i == nombre_i_sgte and desfase_i == desfase_i_sgte):
                # si se cumple, se entra en un fragmento
                in_fragmento = True
                # se rellenan los "útlimos"
                ult_desfase = desfase_i
                # el tiempo de inicio (radio)
                ult_t_inicio = elem_i_struct[0][1]
                # el tiempo de fin (radio)
                ult_t_final = elem_i_struct[0][2]
                # el nombre de canción
                ult_cancion = nombre_i
                # última confianza
                ult_confianza = 1
                # ultimo strikes 
                ult_strikes = 0

            else:
                # si no,  
                # se aumenta el indice
                i+=1
                # y se continua
                continue

        # si es que se está en un fragmento
        elif(in_fragmento and (i != largo_f_lineas-1)):
            # se revisa si el que viene tiene el mismo nombre 
            # se obtiene el elemento siguiente
            elem_i_sgte = f_lineas[i+1]
            # se obtiene como estrcutura
            elem_i_sgte_struct = divide_item(elem_i_sgte)

            # se comparan los nombres
            nombre_i = elem_i_struct[1][0]
            nombre_i_sgte = elem_i_sgte_struct[1][0]

            if(nombre_i == nombre_i_sgte):
                # si se cumple, se actualiza el tiempo final, la confianza y los strikes
                ult_t_final = elem_i_struct[0][2]
                ult_confianza += 1
                ult_strikes = 0
            else:
                # si no se cumple se aumentan los strikes
                ult_strikes += 1

            # si es que los strikes son más que el límite dado, se llegó al fin del fragmento
            if(ult_strikes >= strikes_permitidos):
                # ya no se está en un fragmento
                in_fragmento = False
                # se consigue la duración 
                largo = ult_t_final - ult_t_inicio
                # y se escrbe en el archivo
                print("{}\t{}\t{}\t{}\t{}".format(ult_radio, ult_t_inicio, largo, ult_cancion, ult_confianza), file=archivo)   

        # se aumenta el indice
        i+=1






        




# inicio de la tarea
if len(sys.argv) < 3:
    print("Uso: {} [dir_resultados_knn] [file_resultados_txt]".format(sys.argv[0]))
    sys.exit(1)

dir_resultados_knn = sys.argv[1]
file_resultados_txt = sys.argv[2]

tarea2_deteccion(dir_resultados_knn, file_resultados_txt)
