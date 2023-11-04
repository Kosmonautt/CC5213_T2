malo = "Carlos Gardel - Por una Cabeza (14).m4a.22050.wav"
correcto = "Carlos Gardel - Por una Cabeza (14).m4a"

malo = malo.split(".")

malo = malo[0]+"."+malo[1]

print(malo == correcto)


print(malo)
print(correcto)