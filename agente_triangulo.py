import math
import random
import sys
from os import system,name
import keyboard
from time import sleep

# TODO: [BUGS] Con la funcionalidad de la tecla esc
# [Trabajo Futuro] Evitar que elija un movimiento que acaba de tomar
agente = "/_\\ "

porcentaje_comida = 0.15
porcentaje_obstaculos = 0.10

class Rejilla:
    ''' Mapa 2D para el agente '''
    def __init__(self, dimension):
        self.dimension = dimension
        self.posicion_agente = [0,0]
        self.posicion_anterior = [-1,-1]
        self.rejilla = [['    ' for n in range(dimension)] for m in range(dimension)]
        self.cantidad_comida = math.floor(dimension * dimension * porcentaje_comida)
        self.cantidad_obstaculos = math.floor(dimension * dimension * porcentaje_obstaculos)
        # Distribucion aleatoria de comida y obstaculos
        comidas = [[random.randint(0,dimension-1),random.randint(0,dimension-1)] for x in range(self.cantidad_comida)]
        for c in comidas:
            self.rejilla[c[0]][c[1]] = '  * '
        obstaculos = [[random.randint(0,dimension-1),random.randint(0,dimension-1)] for x in range(self.cantidad_obstaculos)]
        self.obstaculos = obstaculos
        for o in obstaculos:
            self.rejilla[o[0]][o[1]] = '  X '
        if self.detectar_comida():
            self.cantidad_comida = self.cantidad_comida -1
        self.rejilla[self.posicion_agente[0]][self.posicion_agente[1]]=agente


    def ver_rejilla(self):
        if self.posicion_anterior[0] > -1:
            self.rejilla[self.posicion_anterior[0]][self.posicion_anterior[1]] = agente
        for fila in self.rejilla:
            print('+----'*self.dimension,end='')
            print('+')
            for valor in fila:
                print('|'+valor,end=''),

            print('|',end='\n')
        print('+----'*self.dimension)
        print('Comida: ' , self.cantidad_comida)
        print('Agente en: ',self.posicion_agente)
        self.rejilla[self.posicion_anterior[0]][self.posicion_anterior[1]] = '    '
    def detectar_comida(self):
        ''' Retorna True si hay comida en la posicion actual del agente '''
        if self.rejilla[self.posicion_agente[0]][self.posicion_agente[1]] == '  * ':
            return True
        else:
            return False

    def ejecutar_agente(self):
        if self.detectar_comida():
            self.cantidad_comida = self.cantidad_comida -1
        self.rejilla[self.posicion_agente[0]][self.posicion_agente[1]] = agente
        self.mover_agente()

    def simular(self):
        while True:
            self.ver_rejilla()
            self.ejecutar_agente()
            sleep(1)
            clear()
            if keyboard.is_pressed('esc'):
                print('Saliendo...')
                sleep(.500)
                sys.exit(0)

    def mover_agente(self):
        movimientos = [[1,0],
        [-1,0],
        [0,1],
        [0,-1]]
        #solo los movimientos que no se salgan de la rejilla
        self.posicion_anterior = self.posicion_agente
        movimientos_disponibles = [[m[0] + self.posicion_agente[0], m[1] + self.posicion_agente[1]]
            for m in movimientos
            if m[0] + self.posicion_agente[0] > -1 if m[0] + self.posicion_agente[0] < self.dimension
            and
            m[1] + self.posicion_agente[1] > -1 if m[1] + self.posicion_agente[1] < self.dimension]
        #omite las opciones donde hay obstaculos
        movimientos_disponibles = [m for m in movimientos_disponibles if m not in self.obstaculos]
        #finalmente elige un movimiento aleatoriamente
        movimiento = random.choice(movimientos_disponibles)
        #actualiza la posicion del agente
        self.posicion_agente = movimiento




def clear():
    if name == 'nt':
        _ =system('cls')
    else:
        _=system('clear')


def main():
    dimension = int(input('Ingresa la dimension de la rejilla\n(Preferible entre 4 y 10): '))
    if 3 < dimension and dimension < 12:
        r = Rejilla(dimension)
    else:
        print('El tamaño ingresado es muy pequeño o muy grande para visualizar.')
        sys.exit(0)
    print('Presiona ENTER para comenzar y ESC para salir.')
    keyboard.wait('enter')
    r.simular()

if __name__ == '__main__':
    main()
