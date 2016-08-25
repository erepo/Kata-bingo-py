#!/usr/bin/env python

import unittest

import fila


class TestFila(unittest.TestCase):

    def setUp(self):
        self.testFila = fila.Fila()

    def testLaCartaContieneNueveCasillasEnCadaFila(self):
        self.assertEqual(9, self.testFila.length())

    def testCuatroCuadrosBlancosEnLaFila(self):
        blancos = self.testFila.blancos()
        self.assertTrue(self.testFila.esBlanco(0))
        self.assertTrue(self.testFila.esBlanco(1))
        self.assertTrue(self.testFila.esBlanco(2))
        self.assertTrue(self.testFila.esBlanco(3))

    def testCincoCuadrosConNumerosEnLaFila(self):
        numeros = self.testFila.numeros()
        self.assertTrue(self.testFila.esNumero(0))
        self.assertTrue(self.testFila.esNumero(1))
        self.assertTrue(self.testFila.esNumero(2))
        self.assertTrue(self.testFila.esNumero(3))
        self.assertTrue(self.testFila.esNumero(4))

    def tearDown(self):
        del self.testFila