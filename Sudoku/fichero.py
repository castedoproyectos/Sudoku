import csv


class FicheroHandler:

    def __init__(self, nombre):
        self.nombre = nombre
        self.data = []

    def leerFichero(self):
        with open(self.nombre) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=' ')
            contador_filas = 0
            for row in csv_reader:
                contador_filas = contador_filas + 1
                contador_columnas = 0
                for elemento in row:
                    contador_columnas = contador_columnas + 1
                    self.data.append([int(elemento), contador_filas, contador_columnas])

        return self.data
