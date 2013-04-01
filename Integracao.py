from Pai import Pai
from Relogio import Relogio
from Util import Util

from com.android.monkeyrunner import MonkeyRunner

class Integracao():
    
    def __init__(self,vc,device):
        self.vc = vc
        self.device = device
        
        
        
    def calculadora_cronometro(self):
        util = Util(self.device,self.vc)
        
        relogio = Relogio(self.vc,self.device)            
        
        relogio.inicia_cronometro(["3","1"])

        util.trocar_aplicacao("AndroidCalculator")
        
        MonkeyRunner.sleep(25)
        
        self.vc.dump()
        
        self.vc.findViewWithAttributeOrRaise("content-desc","Stop").touch()    
    
        self.vc.dump(2)
        