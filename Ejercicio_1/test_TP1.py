import unittest
import io
import sys
import os
from unittest.mock import patch
from tp1 import TP1


class TestTP1(unittest.TestCase):

    def setUp(self):
        self.tp1 = TP1()

    def test_ejercicio_1(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.tp1.ejercicio_1(5)
            expected_output = '[1, 3, 5, 7, 9]\n'
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_ejercicio_2(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.tp1.ejercicio_2(3, "Hola")
            expected_output = 'HolaHolaHola\n'
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_ejercicio_3(self):
        test_file = 'archivo_test.txt'
        with open(test_file, 'w') as f:
            f.write('Candelabro\nManzana\nVentana')
        with patch('sys.stdout', new=io.StringIO()) as patched_output:
            self.tp1.ejercicio_3(test_file)
            patched_print = 'Cantidad de palabras: 3\nCantidad de líneas: 3\n'
            self.assertEqual(patched_output.getvalue(), patched_print)
            os.remove(test_file)

    def test_ejercicio_3_error(self):
        with patch('sys.stdout', new=io.StringIO()) as patched_output:
            self.tp1.ejercicio_3('archivo_fake.txt')
            with open(errors.log, 'r') as error_log:
                self.tp1.ejercicio_3('archivo_inexistente.txt')
                self.assertEqual(error_log.getvalue(), error_log)

if __name__ == '__main__':
    unittest.main()