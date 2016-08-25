#!/usr/bin/env python

import carta

_COLUMNA_LENGTH = 9;
_BLANCOS_LENGTH = 4;
_NUMEROS_LENGTH = 5;


class Jugador:
    def __init__(self):
        self.bingoCarta = carta.Carta()

    def comprarCarta(self, c):
        isinstance(c, carta.Carta)
        self.bingoCarta = c

    def tieneCarta(self):
        return True

    def notificacionDeNuevoNumero(self, numero):
        line = self.bingoCarta.numeroDeFila(numero)

    def chequeoNumero(self, numero):
        return self.bingoCarta.numeroDeFila(numero)

    def chequeoLineaGanadora(self, numero):
        f = self.chequeoNumero(numero)
        return f