import os, sys, time

"""
1- Escribir un programa que realice la multiplicación de dos matrices de 2x2. 
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado en una fifo indicando el indice del elemento.
El padre deberá leer en la fifo y mostrar el resultado final."""
def multiplicar_matrices(matriz_A, matriz_B, pipe_name):
    try:
        os.mkfifo(pipe_name)
    except FileExistsError:
        pass
    resultado = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            pid = os.fork()
            if pid == 0:
                for k in range(2):
                    resultado[i][j] += matriz_A[i][k] * matriz_B[k][j]
                with open(pipe_name, 'w') as pipe:
                    pipe.write(f'{i}{j}={resultado[i][j]}\n')
                sys.exit()


if __name__ == '__main__':
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    pipe_name = os.getcwd() + 'fifo_matrices'
    pid = os.fork()
    if pid == 0:
        multiplicar_matrices(A, B, pipe_name)
    else:
        print(f'Parent: {pid}')
        os.wait()
        with open(pipe_name, 'r') as pipe:
            linea = ''
            for _ in range(4):
                linea += pipe.readline().replace('\n', ' ') 
            for i in linea.split():
                print(i) 
        os.unlink(pipe_name)