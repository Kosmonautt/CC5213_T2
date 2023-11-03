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


    # # se crea la carpeta para los resultados finales
    # os.makedirs(file_resultados_txt, exist_ok=True)

    # se crea el archivo con los resultados finales 
    archivo = open(file_resultados_txt, 'w+')

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

    for resultado in f_lineas:
        # se divide el resultado por el símbolo |
        resultado_lista = resultado.split("|")
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
        # # intervalo de tiempo
        # cancion_delta = cancion_lista[1]
        # # se consigue el inicio y el final
        # cancion_delta = cancion_delta.split("-")
        # # inicio
        # cancion_inicio = float(cancion_delta[0].strip())
        # # final
        # cancion_final = float(cancion_delta[1].strip())

        # si es que no es None, entonces ya se rellenó el primero
        if(ult_radio != None):
            # se revisa si el nombre de la canción es diferente o el desface es diferente
            if((cancion_nombre != ult_cancion)):
                # si es que es diferente, entonces se debe escribir cuánto duró la ventana de la canción en la radio
                # se consigue la diferencia de tiempo
                largo = ult_t_final - ult_t_inicio
                # se escribe en el archivo 
                print("{}\t{}\t{}\t{}\t{}".format(ult_radio, ult_t_inicio, largo, ult_cancion, ult_confianza), file=archivo)   

                # se consiguen los nuevos valores
                # ultimo desface
                ult_desfase = desface
                # último tiempo de inicio 
                ult_t_inicio = radio_inicio
                # último tiempo de final
                ult_t_final = radio_final
                # último archivo de Q
                ult_radio = radio_nombre
                # último arhcivo de R
                ult_cancion = cancion_nombre
                # última confianza
                ult_confianza = 1   
            # si es que es la misma canción y el mismo desface
            else:
                # se actualiza el útlimo tiempo final
                ult_t_final = radio_final
                # la confianza se aumenta en 1
                ult_confianza += 1

        # si es que la ultima radio es None, entonces se rellena todo y se va al siguiente ciclo
        else:
            # ultimo desface
            ult_desfase = desface
            # último tiempo de inicio 
            ult_t_inicio = radio_inicio
            # último tiempo de final
            ult_t_final = radio_final
            # último archivo de Q
            ult_radio = radio_nombre
            # último arhcivo de R
            ult_cancion = cancion_nombre
            # última confianza
            ult_confianza = 1
        
            




    # Implementar la deteccion
    #  1-leer resultados de knn en dir_resultados_knn
    #  2-buscar secuencias similares entre audios
    #  4-escribir en file_resultados_txt las detecciones encontradas
    #    seguir el formato: print("{}\t{}\t{}\t{}\t{}".format(radio, desde, largo, cancion, confianza))
    # borrar la siguiente linea
    print("ERROR: no implementado!")


# inicio de la tarea
if len(sys.argv) < 3:
    print("Uso: {} [dir_resultados_knn] [file_resultados_txt]".format(sys.argv[0]))
    sys.exit(1)

dir_resultados_knn = sys.argv[1]
file_resultados_txt = sys.argv[2]

tarea2_deteccion(dir_resultados_knn, file_resultados_txt)
