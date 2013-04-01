from Util import Util

class Calculadora():
    
    def __init__(self, vc, device):
        self.vc = vc
        self.device = device
        self.util = Util(self.device,self.vc)
                
        
    
    def multiplicacao(self,primeiro,segundo):
        multiplicacao = primeiro * segundo
                  
        self.vc.dump()
        primeiro_campo = self.vc.findViewWithAttributeOrRaise("content-desc","firstDesc")  
         
        primeiro_campo.type(str(primeiro))
         
        self.vc.findViewWithAttributeOrRaise("content-desc","secondDesc").type(str(segundo))
         
        self.vc.findViewWithTextOrRaise("Multiply").touch()    
         
        self.vc.dump(1)
        
        return float(multiplicacao)
        
        
    def checar_resultado(self,multiplicacao):
        self.vc.dump(1)
         
        resultado = float(self.vc.findViewWithAttributeOrRaise("content-desc","result").getText())
         
        return resultado == multiplicacao
        
        
    def fechando_calculadora(self):
        if self.checar_titulo != None:
            self.device.press("KEYCODE_BACK", self.device.DOWN_AND_UP)
        else:        
            self.util.trocar_aplicacao("AndroidCalculator")
            self.vc.dump(1)
            self.device.press("KEYCODE_BACK", self.device.DOWN_AND_UP)
        
        
        
    def checar_titulo(self):
        titulo = self.vc.findViewWithTextOrRaise("AndroidCalculator")
        return titulo != None
    
        
    def inicia_calculadora(self):
        
        self.device.press("KEYCODE_HOME", self.device.DOWN_AND_UP)
        
        self.vc.dump()
        
        self.vc.findViewWithAttributeOrRaise("content-desc","Apps").touch()
        
        self.vc.dump()
        
        self.vc.findViewWithTextOrRaise("AndroidCalculator").touch()
        
        self.vc.dump()