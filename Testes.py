#! /usr/bin/env monkeyrunner

import sys
import os
import unittest

# this must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails
try:
    for p in os.environ['PYTHONPATH'].split(':'):
        if not p in sys.path:
            sys.path.append(p)
except:
    pass
try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass


from com.dtmilano.android.viewclient import ViewClient, View
from Pai import Pai
from calculadora_pagina_principal import Calculadora_Pagina_Principal
from Integracao import Integracao
from relogio import Relogio

from com.android.monkeyrunner import MonkeyRunner

class Testes(Pai):
    
    
#     def calculo(self):
    def test_calculo(self):
        calculadora = Calculadora_Pagina_Principal(self.vc,self.device)
        calculadora.inicia_calculadora()
        
        
        integracao = Integracao(self.vc,self.device)
        
        primeiro_numero = 11
        segundo_numero = 23
        
        multiplicacao = calculadora.multiplicacao(primeiro_numero,segundo_numero)
        self.assertTrue(calculadora.checar_resultado(multiplicacao))
        
        integracao.calculadora_cronometro(multiplicacao)
        
    def um(self):
#     def test(self):
        relogio = Relogio(self.vc,self.device)
        tempo = ["5","1"]
        
        relogio.inicia_cronometro(tempo)
        
        

    def tearDown(self):
#         pass
        Calculadora_Pagina_Principal(self.vc,self.device).fechando_calculadora()
        
        
        
        
if __name__ == '__main__':
   unittest.main()