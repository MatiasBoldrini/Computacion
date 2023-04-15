# Definir dos matrices A y B de 2x2
import os, sys, time
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

pipe_name = 'operaciones_fifo'
try:
    os.mkfifo(pipe_name)
except FileExistsError:
    pass
# Comprobar que las matrices se pueden multiplicar
resultado = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        pid = os.fork()
        if pid == 0:
            for k in range(2):
                resultado[i][j] += A[i][k] * B[k][j]
            with open(pipe_name, 'w') as pipe:
                pipe.write(f'{i}{j}={resultado[i][j]}\n')
            sys.exit()

with open(pipe_name, 'r') as pipe:
    linea = ''
    resultado = {'00': 0, '01': 0, '10': 0, '11': 0}
    for _ in range(4):
        linea += pipe.readline()
        linea = linea.replace('=', ' ').replace('\n', ' ')  