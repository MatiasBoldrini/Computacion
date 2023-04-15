# Definir dos matrices A y B de 2x2
import os, sys, time


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
                    while True:
                        try:
                            with open(pipe_name, 'w') as pipe:
                                pipe.write(f'{i}{j}={resultado[i][j]}\n')
                            break
                        except BrokenPipeError:
                            print('ERROR')
                sys.exit()


if __name__ == '__main__':
    g= 0
    while(True):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        pipe_name = 'matrices_fifo'
        multiplicar_matrices(A, B, pipe_name)
        time.sleep(0.8)
        with open(pipe_name, 'r') as pipe:
            linea = ''
            for _ in range(4):
                linea += pipe.readline().replace('\n', ' ') 
            for i in linea.split():
                print(i) 
            print(g,'-'*50)
            if not all(x in linea for x in ["00", "01", "10", "11"]):
                break
        g+=1