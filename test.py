import pickle
import numpy as np
import aux_func

d = np.load("eval_t2/datos_dataset_a/descriptores_canciones/Angela Carrasco - Quererte a ti (15).m4a.22050.wav-descriptor.npy")

#print(d.shape)

wea = []

for i in d:
    if len(wea) == 0:
        wea = i
    else:
        wea = np.vstack([wea, i])


with open("eval_t2/datos_dataset_a/descriptores_canciones/Angela Carrasco - Quererte a ti (15).m4a.22050.wav-ventanas.pickle", "rb") as file:
    l_w: list = pickle.load(file)
    # y se añade a las lista de ventanas Q
    l_v = l_w

#print(l_v[0])

print(d.shape)

new_d = np.vstack([d, d])

print(new_d.shape)

