
from fichero import FicheroHandler
from tablero import Tablero

print("-----------------------------------")
print("      RESOLVEDOR DE SUDOKUS        ")
print("-----------------------------------")


file = FicheroHandler('sudoku.txt') 
datos = file.leerFichero()

tablero = Tablero('sudoku.txt')
tablero.set_tablero(datos)

if tablero.resolver_mecanico() == True:
    print("FIN")

else:
    print("HEURISTICA")
    for element in tablero.posiciones:
        element.imprimir()
