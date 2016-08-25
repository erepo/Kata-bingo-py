#!/usr/bin/env python

import carta

_COLUMNA_LENGTH = 9;
_BLANCOS_LENGTH = 4;
_NUMEROS_LENGTH = 5;

class Fila:

    def __init__(self):
        self.cartaInstance = carta.Carta()
        self.numerosArray = []
        self.indicesBlancos = [x*0 for x in range(_BLANCOS_LENGTH)]
        self.indicesNumeros = [self.cartaInstance.randomNumeroParaColumna(x) for x in range(_NUMEROS_LENGTH)]

    def length(self):
        return _COLUMNA_LENGTH

    def blancos(self):
        return self.indicesBlancos

    def esBlanco(self,columna):
        return self.indicesBlancos[columna] == 0

    def numeros(self):
        return self.indicesNumeros

    def esNumero(self,columna):
        return self.indicesNumeros[columna] != 0