from Pai import Pai
from relogio import Relogio
from calculadora_pagina_principal import Calculadora_Pagina_Principal

from com.android.monkeyrunner import MonkeyRunner

class Integracao():
    
    def __init__(self,vc,device):
        self.vc = vc
        self.device = device
        
        
        
    def calculadora_cronometro(self,multiplicacao):
        
        relogio = Relogio(self.vc,self.device)            
        
        relogio.inicia_cronometro(["5","1"])
        
#         calculadora = Calculadora_Pagina_Principal(self.vc,self.device)
#         calculadora.inicia_calculadora()

#chamar o troca aplicacao
        
        MonkeyRunner.sleep(50)
        
        print "saiu"
    
    
        #clicar no stop
        #volta pro teste e checa se est‡ na tela da aplicacao e recheca o resultado