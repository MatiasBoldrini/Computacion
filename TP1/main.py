import argparse
import sys
import datetime


class TP1():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Trabajo Práctico 1: Argumentos')
        parser.add_argument('-a', '--impar', type=int,
                            help='Amount of odd numbers')
        parser.add_argument('-m', '--multiplier', type=int,
                            help='String multiplier')
        parser.add_argument('-s', '--string', type=str,
                            help='string to multiply')
        parser.add_argument('-f', '--file', type=str,
                            help='file to read')
        parser.add_argument('-l', '--low_level', type=str,
                            help='file to read')
        parser.add_argument('-p', '--promedio', action='store_true',
                            help='promedio de palabras')
        args = parser.parse_args()
        if args.impar:
            self.ejercicio_1(args.impar)
        if args.multiplier and args.string:
            self.ejercicio_2(args.multiplier, args.string)
        if args.file:
            self.ejercicio_3(args.file, args.promedio)
        if args.low_level:
            self.ejercicio_4(args.low_level)

    def ejercicio_1(self, n):
        """ 
            Escribir un programa en Python que acepte un número de argumento entero positivo n y genere una lista de los n primeros números impares. 
            El programa debe imprimir la lista resultante en la salida estandar.
            """
        print([i for i in range(1, n*2, 2)])

    def ejercicio_2(self, multiplier, string):
        """ 
        Escribir un programa en Python que acepte dos argumentos de línea de comando: una cadena de texto, un número entero. 
        El programa debe imprimir una repetición de la cadena de texto tantas veces como el número entero.
        """
        print(string * multiplier)

    def ejercicio_3(self, archivo, promedio=False):
        """ 
            Escribir un programa en Python que acepte argumentos de línea de comando para leer un archivo de texto. 
            El programa debe contar el número de palabras y líneas del archivo e imprimirlas en la salida estándar. 
            Además el programa debe aceptar una opción para imprimir la longitud promedio de las palabras del archivo. 
            Esta última opción no debe ser obligatoria. 
            Si hubiese errores deben guardarse el un archivo cuyo nombre será "errors.log" usando la redirección de la salida de error.
            """
        with open(archivo, 'r') as f:
            file_content = f.read()
            print(f"Cantidad de palabras: {len(file_content.split())}")
            print(f"Cantidad de líneas: {len(file_content.splitlines())}")
            words_prom = round(len(file_content) / len(file_content.split()))
            if promedio:
                print(f'Longitud promedio de las palabras: {words_prom}')

    def ejercicio_4(self, mensaje):
        """ 
            Continuar el ejercicio comenzado en clase para utilizar la salida de bajo nivel. 
            """
        encoded_message = mensaje.encode('utf-8')
        sys.stdout.buffer.write(encoded_message)


if __name__ == '__main__':
    try:
        tp1 = TP1()
    except Exception as e:
        with open('errors.log', 'a') as f:
            now = datetime.datetime.now()
            formatted_date = datetime.datetime.strftime(
                now, '%y-%m-%d')  # Fecha : 21-03-01
            f.write(f"\n[[ {formatted_date} ]]\n")
            f.write(f"ERROR: {type(e).__name__}\n")
            f.write(f"DESCRIPTION: {str(e)}\n")
