"""1- Escribir un programa en Python que comunique dos procesos.
El proceso padre deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo a través de un pipe. 
El proceso hijo deberá recibir las líneas del archivo y, por cada una de ellas, contar la cantidad de palabras que contiene y mostrar ese número."""

import os
import time
fdr, fdw = os.pipe()
pid = os.fork()
if pid == 0:
    os.close(fdw)
    while True:
        linea = os.read(fdr, 2024)
        if not linea:
            break
        print(f'{linea.strip().decode()}" tiene {len(linea.split())} palabras') 
        #os.write(1, b'1')

    exit()
os.close(fdr)
with open('textfile.txt', 'r') as f:
    for line in f:
        os.write(fdw, bytes(line, 'utf8'))
        #os.read(fdr, 1)
        time.sleep(0.2)
