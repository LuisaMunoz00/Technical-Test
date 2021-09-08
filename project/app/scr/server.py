from random import *
import string, os

nombres_archivos = []

numero_archivos = randint(10,20)
longitud_nombre = 8
for x in range(numero_archivos):
   nombre_archivo = ".join(choice(string.ascii_letters + string.digits) for _ in range(logintud_nombre))
   nombres_archivos.append(nombre_archivo)

print(nombres_archivos)
print("numero de archivos creados:", len (nombres_archivos))

for i in nombres_archivos:
   nombre = str(i) + ".txt"
   txt = open(
