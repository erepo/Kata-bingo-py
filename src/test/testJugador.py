#!/usr/bin/env python
import unittest
from mock import MagicMock
from random import randint
from jugador import Jugador
from carta import Carta
from bombo import Bombo

class TestJugador(unittest.TestCase):

    def setUp(self):
        self.jugador = Jugador()
        self.bomboMocked = MagicMock(Bombo)
        self.cartaMocked = MagicMock(Carta)

    def testJugadorCompraCarta(self):
        self.jugador.comprarCarta(self.cartaMocked)
        self.assertTrue(self.jugador.tieneCarta())

    def testChequeoDeNumeroMismaFila(self):
        numeroFila = 1 #seteo de la fila
        self.cartaMocked.numeroDeFila = MagicMock(return_value=numeroFila)
        self.cartaMocked.numeroDeFila(numeroFila)
        self.cartaMocked.numeroDeFila.assert_called_once_with(numeroFila) # chequeo de llamada solo 1 vez al metodo
        numeroEnLaFila=8 #seteo del numero en la fila
        self.bomboMocked.getNumero = MagicMock(return_value=numeroEnLaFila)
        self.bomboMocked.getNumero(numeroEnLaFila)
        self.bomboMocked.getNumero.assert_called_once_with(numeroEnLaFila) # chequeo de llamada solo 1 vez al metodo

        self.jugador.comprarCarta(self.cartaMocked)

        self.assertEquals(1,self.jugador.chequeoNumero(self.bomboMocked.getNumero))

    def testChequeoDeLlamadaDeNumeroEnLaFila(self):
        anyInt = randint(0,9)
        self.jugador.comprarCarta(self.cartaMocked)
        self.jugador.chequeoNumero(anyInt)

        anyIntFila = randint(0, 3)
        self.cartaMocked.numeroDeFila = MagicMock(return_value=anyIntFila)
        self.cartaMocked.numeroDeFila(anyIntFila)
        self.cartaMocked.numeroDeFila.assert_called_with(anyIntFila)

    def testChequeoDeNumeroNoEstaEnNingunaFila(self):
        numeroFila = -1  # seteo de la fila
        self.cartaMocked.numeroDeFila = MagicMock(return_value=numeroFila)
        self.cartaMocked.numeroDeFila(numeroFila)
        self.cartaMocked.numeroDeFila.assert_called_once_with(numeroFila)  # chequeo de llamada solo 1 vez al metodo
        numeroEnLaFila = 8  # seteo del numero en la fila
        self.bomboMocked.getNumero = MagicMock(return_value=numeroEnLaFila)
        self.bomboMocked.getNumero(numeroEnLaFila)
        self.bomboMocked.getNumero.assert_called_once_with(numeroEnLaFila)  # chequeo de llamada solo 1 vez al metodo

        self.jugador.comprarCarta(self.cartaMocked)

        self.assertEquals(-1,self.jugador.chequeoNumero(self.bomboMocked.getNumero))
        pass

    def testJugadorChequeaNumeroYVericaSiTieneLineaGanadora(self):
        anyInt = randint(0,3)
        self.jugador.comprarCarta(self.cartaMocked)
        self.jugador.chequeoLineaGanadora(anyInt)

        self.cartaMocked.numeroDeFila = MagicMock(return_value=anyInt)
        self.cartaMocked.numeroDeFila(anyInt)
        self.cartaMocked.numeroDeFila.assert_called_with(anyInt)

    def tearDown(self):
        del self.jugador