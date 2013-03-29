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


from com.android.monkeyrunner import MonkeyRunner

class Testes(Pai):
    
    def test_calculo(self):
        principal = Calculadora_Pagina_Principal(self.vc,self.device)
        integracao = Integracao(self.vc,self.device)
        
        primeiro_numero = 1
        segundo_numero = 10
        
        multiplicacao = principal.multiplicacao(primeiro_numero,segundo_numero)
        self.assertTrue(principal.checar_resultado(multiplicacao))
        
        integracao.calculadora_cronometro(multiplicacao)
        

    def tearDown(self):
        Calculadora_Pagina_Principal(self.vc,self.device).fechando_calculadora()
        
        
        
        
if __name__ == '__main__':
   unittest.main()