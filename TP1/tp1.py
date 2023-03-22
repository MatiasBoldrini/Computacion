import argparse


class TP1():
    def __init__(self):
        parser = argparse.ArgumentParser(description='TP1')
        parser.add_argument('-a', '--impar', type=int,
                            help='Amount of odd numbers')
        parser.add_argument('-m', '--multiplier', type=int,
                            help='String multiplier')
        parser.add_argument('-s', '--string', type=str,
                            help='string to multiply')
        args = parser.parse_args()
        if args.impar:
            self.ejercicio_1(args.impar)
        if args.multiplier and args.string:
            self.ejercicio_2(args.multiplier, args.string)

    def ejercicio_1(self, n):
        """ 
            Escribir un programa en Python que acepte un número de argumento entero positivo n y genere una lista de los n primeros números impares. El programa debe imprimir la lista resultante en la salida estandar.
            """
        print([i for i in range(1, n*2, 2)])

    def ejercicio_2(self, multiplier, string):
        """ 
        Escribir un programa en Python que acepte dos argumentos de línea de comando: una cadena de texto, un número entero. El programa debe imprimir una repetición de la cadena de texto tantas veces como el número entero.
        """
        print(string * multiplier)

    def ejercicio_3(self, archivo):
        """ 
            Escribir un programa en Python que acepte argumentos de línea de comando para leer un archivo de texto. El programa debe contar el número de palabras y líneas del archivo e imprimirlas en la salida estándar. Además el programa debe aceptar una opción para imprimir la longitud promedio de las palabras del archivo. Esta última opción no debe ser obligatoria. Si hubiese errores deben guardarse el un archivo cuyo nombre será "errors.log" usando la redirección de la salida de error.
            """

        pass

    def ejercicio_4(self, archivo):
        """ 
            Continuar el ejercicio comenzado en clase para utilizar la salida de bajo nivel. 
            """
        pass


if __name__ == '__main__':
    tp1 = TP1()
