import unittest
from io import StringIO
import sys, os, patch
from tp1 import TP1


class TestTP1(unittest.TestCase):
    def test_ejercicio_1(self):
        # Verifica que se genera la lista correcta de números impares
        tp1 = TP1()
        expected_output = '[1, 3, 5, 7, 9]\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            tp1.ejercicio_1(5)
            output = fake_stdout.getvalue()
        self.assertEqual(output, expected_output)

    def test_ejercicio_2(self):
        # Verifica que se imprime la cadena repetida correctamente
        tp1 = TP1()
        expected_output = 'hola hola hola hola hola \n'
        with StringIO() as buffer:
            sys.stdout = buffer
            tp1.ejercicio_2(5, 'hola ')
            output = buffer.getvalue()
        self.assertEqual(output, expected_output)

    # def test_ejercicio_3(self):
    #     # Verifica que se cuenta correctamente el número de palabras y líneas en el archivo de texto
    #     tp1 = TP1()
    #     expected_output = 'Number of lines: 3\nNumber of words: 8\n'
    #     with StringIO() as buffer:
    #         sys.stdout = buffer
    #         tp1.ejercicio_3('test_file.txt')
    #         output = buffer.getvalue()
    #     self.assertEqual(output, expected_output)

    # def test_ejercicio_4(self):
    #     # Verifica que se escribe correctamente el archivo binario a partir de un archivo de texto
    #     tp1 = TP1()
    #     expected_output = 'Binary file written successfully\n'
    #     with StringIO() as buffer:
    #         sys.stdout = buffer
    #         tp1.ejercicio_4('test_file.txt')
    #         output = buffer.getvalue()
    #     self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()