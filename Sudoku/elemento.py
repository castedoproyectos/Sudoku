class Elemento:

    def __init__(self, numero, fila, columna):
        self.numero = numero
        self.fila = fila
        self.columna = columna
        self.check = False

        if self.numero == 0:
            self.posibilidades = [1,2,3,4,5,6,7,8,9]
        else:
            self.posibilidades = []

        if fila < 4:
            if columna < 4:
                self.cuadrado = 1
            elif columna < 7:
                self.cuadrado = 2
            else:
                self.cuadrado = 3
        elif fila < 7:
            if columna < 4:
                self.cuadrado = 4
            elif columna < 7:
                self.cuadrado = 5
            else:
                self.cuadrado = 6
        else:
            if columna < 4:
                self.cuadrado = 7
            elif columna < 7:
                self.cuadrado = 8
            else:
                self.cuadrado = 9


    def set_numero(self, numero):
        self.numero = numero

    def get_numero(self):
        return self.numero

    def fijar_numero(self):
        if len(self.posibilidades) == 1:
            self.numero = self.posibilidades[0]
            return True
        else:
            return False

    def imprimir(self):
        print("Elemento -> " + str(self.numero) + " " + str(self.fila) + " " + str(self.columna) + " " + str(self.cuadrado) + " " + str(self.posibilidades))
