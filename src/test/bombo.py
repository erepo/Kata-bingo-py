#!/usr/bin/env python

from random import randint

from jugador import Jugador

_NUM_BOLAS_EN_BOMBO = 89

class Bombo:

    def __init__(self):
        self.bomboNumeros = []
        self.jugadores = []
        self._poblarBombo()

    def getNumero(self):
        if len(self.bomboNumeros) == 0:
            return -1 #el bombo esta vacio
        else:
            indice = randint(0,len(self.bomboNumeros)-1)
            numero = self.bomboNumeros[indice] #extraigo el numero
            self.bomboNumeros.pop(indice) #se elimina la bola del bombo
        return numero

    def _poblarBombo(self):
        self.bomboNumeros = [x for x in range(_NUM_BOLAS_EN_BOMBO)]

    def addJugador(self, persona):
        isinstance(persona,Jugador)
        self.jugadores.append(persona)