# CC5213 - TAREA 2
# 30 de octubre de 2023
# Alumno: Benjamín Contreras S.

import sys
import os.path
import subprocess
import pickle
import numpy as np


import aux_func

# sample rate de los archivos wav a crear
sample_rate = 22050
# sample size de cada ventana de los descriptores
samples_por_ventana = 4096
# salto de cada sample (igual al anterior para no tener overlap)
samples_salto = 4096
# dimensión del MFCC
dimension = 10


def convertir_a_wav(archivo_audio, sample_rate, dir_temporal):
    archivo_wav = "{}{}.{}.wav".format(dir_temporal, os.path.basename(archivo_audio), sample_rate)
    # verificar si ya esta creado
    if os.path.isfile(archivo_wav):
        return archivo_wav
    comando = ["ffmpeg", "-i", archivo_audio, "-ac", "1", "-ar", str(sample_rate), archivo_wav]
    print("INICIANDO: {}".format(" ".join(comando)))
    proc = subprocess.run(comando, stderr=subprocess.STDOUT)
    if proc.returncode != 0:
        raise Exception("Error ({}) en comando: {}".format(proc.returncode, " ".join(comando)))
    return archivo_wav


def tarea2_extractor(dir_audios, dir_descriptores):
    if not os.path.isdir(dir_audios):
        print("ERROR: no existe directorio {}".format(dir_audios))
        sys.exit(1)
    elif os.path.exists(dir_descriptores):
        print("ERROR: ya existe directorio {}".format(dir_descriptores))
        sys.exit(1)

    # lista con la dirección de los audios
    audios_m4a_dir = []
    # para cada archivo en el directorio de audios, se guarda su dirección en la lista
    for audio in os.listdir(dir_audios):
        # se consigue la dirección del audio
        audio_dir = "{}{}".format(dir_audios, audio)
        # se añade a la lista de direcciones
        audios_m4a_dir.append(audio_dir)

    # se crea el directorio donde se guardarán los archivos wav
    os.makedirs(dir_descriptores, exist_ok=True)

    # lista con la dirección de los audios wav
    audios_wav_dir = []

    # para cada audio, se transforma a wav
    for audio_dir in audios_m4a_dir:
        # se convierte a wav con sample rate de 22050, en el directorio indicado y se guarda su dirección
        audio_wav = convertir_a_wav(audio_dir, sample_rate, dir_descriptores)
        # se añade a la lista
        audios_wav_dir.append(audio_wav)


    # para cada audio wav, se crean sus descriptores
    for audio_wav_dir in audios_wav_dir:
        # se crean sus descriptores
        descriptores = aux_func.calcular_descriptores_mfcc(audio_wav_dir, sample_rate, samples_por_ventana, samples_salto, dimension)


        # se divide la dirección por el "/"
        nombre = audio_wav_dir.split("/")
        # se consigue el nombre del archivo
        nombre = nombre[len(nombre)-1]

        # se crea sus ventanas para tener el audio al que corresponde y a qué fragmento
        ventanas = aux_func.lista_ventanas(nombre, descriptores.shape[0], sample_rate, samples_por_ventana)
        # se cambia el nombre a .pickle
        nombre_pickle = "{}-ventanas.pickle".format(nombre)
        # se guarda el archivo pickle con las ventans en la dirección
        with open(dir_descriptores+"/"+nombre_pickle, "wb") as file:
            pickle.dump(ventanas, file)

        # se cambia el nombre a .npy
        nombre_npy = "{}-descriptor.npy".format(nombre)
        # se guarda el archivo npy con el descriptor en la dirección
        np.save(dir_descriptores+"/"+nombre_npy, descriptores)

# inicio de la tarea
if len(sys.argv) < 3:
    print("Uso: {} [dir_audios] [dir_descriptores]".format(sys.argv[0]))
    sys.exit(1)

dir_audios = sys.argv[1]
dir_descriptores = sys.argv[2]

tarea2_extractor(dir_audios, dir_descriptores)
