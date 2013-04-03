#! /usr/bin/env monkeyrunner

import unittest
import Config

Config.importar()



from com.dtmilano.android.viewclient import ViewClient, View
from Pai import Pai
from Calculadora import Calculadora
from Integracao import Integracao
from Relogio import Relogio


class TestesCalculadora(Pai):
    '''
    Classe responsavel pelos testes da calculadora
    '''
    
    def setUp(self):
        '''
        Chama o setup do Pai e instala a calculadora
        '''
        super(TestesCalculadora,self).setUp()
        calculadora = Calculadora(self.vc,self.device)
        calculadora.instala_calculadora()
    
    
    def test_calculadora_cronometro(self):
        '''
        Teste de integracao entre a calculadora e o cronometro
        '''
        
        calculadora = Calculadora(self.vc,self.device)
        integracao = Integracao(self.vc,self.device)
        
        primeiro_numero = 11
        segundo_numero = 23
        
        multiplicacao = calculadora.multiplicacao(primeiro_numero,segundo_numero)
        
        integracao.calculadora_cronometro()
        
        self.assertTrue(calculadora.checar_titulo)
        self.assertTrue(calculadora.checar_resultado(multiplicacao))
        

    def tearDown(self):
        '''
        Sobrescreve o metodo do Pai e fecha a calculadora
        '''
        
        Calculadora(self.vc,self.device).fechando_calculadora()
        
        
        
        
if __name__ == '__main__':
   unittest.main()