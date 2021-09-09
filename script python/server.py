import random, string, os

nombres_archivos = []

numero_archivos = random.randint(10,20)
longitud_nombre = 8
for x in range(numero_archivos):
   nombre_archivo = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(longitud_nombre))
   nombres_archivos.append(nombre_archivo)

print(nombres_archivos)
print("numero de archivos creados:", len (nombres_archivos))

for i in nombres_archivos:
   nombre = str(i) + ".txt"
   txt = open(r"D:/" + nombre, 'w')
   numero_caracteres = random.randint(1000,5000)
   escritura = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(numero_caracteres))
   txt.write(escritura)
   txt.close