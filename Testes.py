#! /usr/bin/env monkeyrunner

import unittest
import Config

Config.importar()

from com.dtmilano.android.viewclient import ViewClient, View
from Pai import Pai
from Calculadora import Calculadora
from Integracao import Integracao
from Relogio import Relogio


class Testes(Pai):
    
    
    def calculo(self):
#     def test_calculo(self):
        calculadora = Calculadora(self.vc,self.device)
        integracao = Integracao(self.vc,self.device)
        
        calculadora.inicia_calculadora()
        
        primeiro_numero = 11
        segundo_numero = 23
        
        multiplicacao = calculadora.multiplicacao(primeiro_numero,segundo_numero)
        self.assertTrue(calculadora.checar_resultado(multiplicacao))
        
        integracao.calculadora_cronometro()
        
        self.assertTrue(calculadora.checar_titulo)
        self.assertTrue(calculadora.checar_resultado(multiplicacao))        
        

    def tearDown(self):
#         pass
        Calculadora(self.vc,self.device).fechando_calculadora()
        
        
        
        
if __name__ == '__main__':
   unittest.main()