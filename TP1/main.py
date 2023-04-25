"""1- Escribir un programa en Python que comunique dos procesos.
El proceso padre deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo a través de un pipe. 
El proceso hijo deberá recibir las líneas del archivo y, por cada una de ellas, contar la cantidad de palabras que contiene y mostrar ese número."""

"""El programa deberá generar tantos procesos hijos como líneas tenga el archivo de texto.
El programa deberá enviarle, vía pipes (os.pipe()), cada línea del archivo a un hijo.
Cada hijo deberá invertir el orden de las letras de la línea recibida, y se lo enviará al proceso padre nuevamente, también usando os.pipe().
El proceso padre deberá esperar a que terminen todos los hijos, y mostrará por pantalla las líneas invertidas que recibió por pipe."""

import os, time, argparse


def read_line(fd):
    linea = b""
    while True:
        char = os.read(fd, 1)
        linea += char
        if char in [b"", b"\n"]:
            return linea


def main_2(file):
    final_text = b""
    procesos = []
    for line in file.readlines():
        r1, w1 = os.pipe()
        r2, w2 = os.pipe()
        pid = os.fork()
        if pid == 0:
            os.close(w1)
            os.close(r2)
            linea = read_line(r1)
            os.write(w2, linea[::-1].strip() + b"\n")
            #print(os.getpid(), "dd", linea[::-1].strip())
            os._exit(0)
        else:
            procesos.append(pid)
            if b"\n" not in line:
                line += b"\n"
            os.write(w1, line)
            # time.sleep(0.01)
            final_text += read_line(r2)
    print(final_text.decode("utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="archivo a procesar", required=True)
    args = parser.parse_args()

    try:
        with open(args.file, "rb") as file:
            main_2(file)
    except FileNotFoundError:
        print(f"No se encontró el archivo {args.file}")
    except PermissionError:
        print(f"No se tiene permiso para abrir el archivo {args.file}")
    except IsADirectoryError:
        print(f"{args.file} es un directorio, no un archivo")


if __name__ == "__main__":
    main()
