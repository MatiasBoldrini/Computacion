import os
import random
import math
import cmath
import argparse
import time


class Proceso():
    """ Realizar un programa que implemente fork junto con el parseo de argumentos.
    Deberá realizar relizar un fork si -f aparece entre las opciones al ejecutar el programa. 
    El proceso padre deberá calcular la raiz cuadrada positiva de un numero y el hijo la raiz negativa."""

    def __init__(self):
        number = random.randint(1, 1000)
        print(f'PPID: {os.getpid()}')
        print(f'El numero a calcular es {number}')
        pid = os.fork()
        # pstree -g2 -s main.py
        if pid > 0:
            print(f'PADRE: {round(math.sqrt(number),3)}')
        else:
            negative_sqrt = cmath.sqrt(-number)
            print(
                f'HIJO: {round(negative_sqrt.real, 3)} {round(negative_sqrt.imag, 3)*1j}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fork", help="fork", action="store_true")
    args = parser.parse_args()
    proceso = Proceso()
