#!/usr/bin/env python

import fila
from random import randint

_FILA_LENGTH = 3;

class Carta:

    def __init__(self):
        self.fila = []

    def filas(self):
        return _FILA_LENGTH

    def randomNumeroParaColumna(self,columna):
        if columna == 0:
            numero = randint(1,9)
        else:
            numero = columna*10 + randint(0,9)
        return numero

    def numeroDeFila(self,numero):
        f = fila.Fila()
        for i in range(_FILA_LENGTH):
            if (f.esNumero(numero)):
                return i
        else:
            return -1