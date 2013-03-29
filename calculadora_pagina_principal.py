from Util import Util

class Calculadora_Pagina_Principal():
    
    def __init__(self, vc, device):
        self.vc = vc
        self.device = device
        self.util = Util(self.device,self.vc)
    
    def multiplicacao(self,primeiro,segundo):
        multiplicacao = primeiro * segundo
                  
        self.vc.dump()
        first = self.vc.findViewWithAttributeOrRaise("content-desc","firstDesc")
         
        first.type(str(primeiro))
         
        self.vc.findViewWithAttributeOrRaise("content-desc","secondDesc").type(str(segundo))
         
        self.vc.findViewWithTextOrRaise("Multiply").touch()    
         
        self.vc.dump(1)
        
        return float(multiplicacao)
        
        
    def checar_resultado(self,multiplicacao):
        self.vc.dump(1)
         
        resultado = float(self.vc.findViewWithAttributeOrRaise("content-desc","result").getText())
         
        if resultado == multiplicacao:
            return True
        else:
            return False
        
        
    def fechando_calculadora(self):        
        self.util.trocar_aplicacao("AndroidCalculator")
        self.vc.dump(1)
        self.device.press("KEYCODE_BACK", self.device.DOWN_AND_UP)