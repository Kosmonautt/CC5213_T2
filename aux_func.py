import librosa

def calcular_descriptores_mfcc(archivo_wav, sample_rate, samples_por_ventana, samples_salto, dimension):
    # se lee el audio en la dirección dada con librosa, se usa el sample rate del archivo wav
    samples, sr = librosa.load(archivo_wav, sr=None)
    # # se imprimen detalles del archivo (n de samples, sample rate y largo en segundos)
    # print("audio samples={} samplerate={} segundos={:.1f}".format(len(samples), sr, len(samples) / sr))
    # calcular MFCC, con las sambles del wav, su sample rate, dimensión, n de samples por ventana y cuánto avanza por salto
    mfcc = librosa.feature.mfcc(y=samples, sr=sr, n_mfcc=dimension, n_fft=samples_por_ventana, hop_length=samples_salto)
    # convertir a descriptores por fila
    descriptores = mfcc.transpose()

    # se borra la primera columna
    descriptores = descriptores[:,1:]

    return descriptores

# crea un objeto ventana que almacena el nombre de la canción, y el tiempo desde que empieza hasta que termina el sample
class Ventana:
    def __init__(self, nombre_archivo, segundos_desde, segundos_hasta):
        self.nombre_archivo = nombre_archivo
        self.segundos_desde = segundos_desde
        self.segundos_hasta = segundos_hasta
    
    def __str__(self):
        return "{};{:6.3f}-{:6.3f}".format(self.nombre_archivo, self.segundos_desde, self.segundos_hasta)
    
# crea una lista de ventanas para un audio
def lista_ventanas(nombre_archivo, numero_descriptores, sample_rate, samples_por_ventana):
    # tantas ventanas como numero de descriptores
    tiempos = []
    for i in range(0, samples_por_ventana * numero_descriptores, samples_por_ventana):
        # tiempo de inicio de la ventana
        segundos_desde = i / sample_rate
        # tiempo de fin de la ventana
        segundos_hasta = (i + samples_por_ventana - 1) / sample_rate
        # crear objeto
        v = Ventana(nombre_archivo, segundos_desde, segundos_hasta)
        # agregar a la lista
        tiempos.append(v)
    return tiempos