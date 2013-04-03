from Pai import Pai
from Relogio import Relogio
from Util import Util

from com.android.monkeyrunner import MonkeyRunner

class Integracao():
    '''
    Classe responsavel pela integracao entre as aplicacoes
    '''
    
    def __init__(self,vc,device):
        '''
        Construtor
        
        @type vc: ViewClient
        @param vc: instancia do viewclient
        
        @type device: MonkeyDevice
        @param device: instancia do monkeyDevice 
        '''
        
        self.vc = vc
        self.device = device
        
        
        
    def calculadora_cronometro(self):
        '''
        Inicia o cronometro e volta para a calculadora
        '''
    
        util = Util(self.device,self.vc)
        
        relogio = Relogio(self.vc,self.device)            
        
        relogio.inicia_cronometro(["2","1"])

        util.trocar_aplicacao("AndroidCalculator")
        
        self.vc.dump(-1,20)
        
        self.vc.findViewWithAttribute("content-desc","Stop").touch()    
    
        self.vc.dump()
