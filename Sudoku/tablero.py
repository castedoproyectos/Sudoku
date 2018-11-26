from elemento import Elemento

class Tablero:

    def __init__(self,nombre):
        self.nombre = nombre
        self.posiciones = []
        self.posicionesFin = []

    def set_tablero(self, elementos):
        for elemento in elementos:
            self.posiciones.append(Elemento(elemento[0], elemento[1], elemento[2]))

    def add_posicion(self, elemento):
        self.posiciones.append(elemento)

    def add_posicion(self, numero, fila, columna):
        newElemento = Elemento(numero,fila,columna)
        self.posiciones.append(newElemento)


    def limpar_elemento(self, elemento):
        for elem in self.posiciones:
            if elemento.fila == elem.fila:
                # Eliminacion del elemento
                if elemento.numero in elem.posibilidades:
                    pos = elem.posibilidades.index(elemento.numero)
                    del elem.posibilidades[pos]
                    if len(elem.posibilidades) == 1:
                        elem.numero = elem.posibilidades[0]
                        del elem.posibilidades[0]


            elif elemento.columna == elem.columna:
                # Eliminacion del elemento
                if elemento.numero in elem.posibilidades:
                    pos = elem.posibilidades.index(elemento.numero)
                    del elem.posibilidades[pos]
                    if len(elem.posibilidades) == 1:
                        elem.numero = elem.posibilidades[0]
                        del elem.posibilidades[0]

            elif elemento.cuadrado == elem.cuadrado:
                # Eliminacion del elemento
                if elemento.numero in elem.posibilidades:
                    pos = elem.posibilidades.index(elemento.numero)
                    del elem.posibilidades[pos]
                    if len(elem.posibilidades) == 1:
                        elem.numero = elem.posibilidades[0]
                        del elem.posibilidades[0]


    def resolver_mecanico(self):
        i = 0
        while i < len(self.posiciones):
            pos = self.posiciones[i]

            if pos.numero != 0:
                self.limpar_elemento(pos)
                self.posicionesFin.append(pos)
                i = self.posiciones.index(pos)
                del self.posiciones[i]
                i = 0
            else:
                i = i + 1

        if len(self.posiciones) == 0:
            print("  SOLUCION ENCONTRADA: ")
            self.print_solucion()
            return True
        else:
            return False


    def print_solucion(self):
        solucion = self.posicionesFin

        fila = []

        num_fila = 1
        num_columna = 1

        while len(solucion) > 0:
            for element in solucion:
                if element.fila == num_fila and element.columna == num_columna:
                    fila.append(element.numero)
                    num_columna = num_columna + 1

                    pos = solucion.index(element)
                    del solucion[pos]

                    if num_columna > 9:
                        num_columna = 1
                        num_fila = num_fila + 1

                        print(fila)
                        fila.clear()

 #  def actualizar_posibilidades(self):


 #   def resolverFilas(self):

