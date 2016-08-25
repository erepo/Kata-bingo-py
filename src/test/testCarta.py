#!/usr/bin/env python

import unittest
from carta import Carta

class Testcarta(unittest.TestCase):

    def setUp(self):
        self.testCarta = Carta()

    def testNumeroDeFilasCorrectas(self):
        self.assertEquals(3, self.testCarta.filas())

    def testLimiteInferiorYSuperiorPrimeraColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(0) > 0)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(0) <= 9)

    def testLimiteInferiorYSuperiorSegundaColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(1) >= 10)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(1) <= 19)

    def testLimiteInferiorYSuperiorTerceraColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(2) >= 20)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(2) <= 29)

    def testLimiteInferiorYSuperiorCuartaColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(3) >= 30)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(3) <= 39)

    def testLimiteInferiorYSuperiorQuintaColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(4) >= 40)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(4) <= 49)

    def testLimiteInferiorYSuperiorSextaColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(5) >= 50)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(5) <= 59)

    def testLimiteInferiorYSuperiorSeptimaColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(6) >= 60)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(6) <= 69)

    def testLimiteInferiorYSuperiorOctavaColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(7) >= 70)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(7) <= 79)

    def testLimiteInferiorYSuperiorNovenaColumna(self):
        self.assertTrue(self.testCarta.randomNumeroParaColumna(8) >= 80)
        self.assertTrue(self.testCarta.randomNumeroParaColumna(8) <= 89)

    def tearDown(self):
        del self.testCarta