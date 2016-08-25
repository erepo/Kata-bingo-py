#!/usr/bin/env python

import unittest
from mock import MagicMock
import bombo
import jugador


class TestBombo(unittest.TestCase):

    def setUp(self):
        self.bingoBombo = bombo.Bombo()
        self.jugadorMock = MagicMock(jugador.Jugador)

    def testObtenerNumeroDesdeBombo(self):
        numero = self.bingoBombo.getNumero()
        self.assertNotEqual(numero,-1)

    def testDosExtraccionesConsecutivasDiferentesNumeros(self):
        numero1 = self.bingoBombo.getNumero()
        numero2 = self.bingoBombo.getNumero()
        self.assertTrue(numero1 != numero2)

    def testTresExtraccionesConsecutivasDiferentesNumeros(self):
        numero1 = self.bingoBombo.getNumero()
        numero2 = self.bingoBombo.getNumero()
        numero3 = self.bingoBombo.getNumero()
        self.assertTrue(numero1 != numero2)
        self.assertTrue(numero1 != numero3)
        self.assertTrue(numero2 != numero3)

    def testBingoNotificaAJugadorCuandoHayNuevoNumero(self):
        self.bingoBombo.addJugador(self.jugadorMock)
        numero = self.bingoBombo.getNumero()
        self.jugadorMock.notificacionDeNuevoNumero = MagicMock(return_value=numero)
        self.jugadorMock.notificacionDeNuevoNumero(numero)
        self.jugadorMock.notificacionDeNuevoNumero.assert_called_with(numero)

    def testBomboDeberiaEstarVacio(self):
        for i in range(len(self.bingoBombo.bomboNumeros)):
            self.bingoBombo.getNumero()
        self.assertTrue(self.bingoBombo.getNumero() == -1)

    def tearDown(self):
        del self.bingoBombo