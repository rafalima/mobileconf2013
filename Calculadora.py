import Config
from Util import Util

class Calculadora():
    
    def __init__(self, vc, device):
        self.vc = vc
        self.device = device
        self.util = Util(self.device,self.vc)
                
    def instala_calculadora(self):
        caminho_apk = self.device.shell('pm path com.calculator')
        if caminho_apk.startswith('package:'):
            print "calculadora instalada."
        else:
            print "calculadora nao instalada, instalando..."
            configs = Config.ambiente()
            self.device.installPackage(configs['arquivo_apk'])
            
    def inicia_calculadora(self):
        
        self.device.press("KEYCODE_HOME", self.device.DOWN_AND_UP)
        
        self.vc.dump()
        
        self.vc.findViewWithAttribute("content-desc","Apps").touch()
        
        self.vc.dump()
        
        self.vc.findViewWithText("AndroidCalculator").touch()
        
        self.vc.dump()
        
    
    def multiplicacao(self,primeiro,segundo):
        self.inicia_calculadora()
        
        multiplicacao = primeiro * segundo
                  
        self.vc.dump()
        
        primeiro_campo = self.vc.findViewWithAttribute("content-desc","firstDesc")
        
        self.limpar_campo(primeiro_campo)  
         
        primeiro_campo.type(str(primeiro))
         
        segundo_campo = self.vc.findViewWithAttribute("content-desc","secondDesc")
        
        self.limpar_campo(segundo_campo)
        
        segundo_campo.type(str(segundo))
         
        self.vc.findViewWithText("Multiply").touch()    
         
        self.vc.dump()
        
        return float(multiplicacao)
        
        
    def checar_resultado(self,multiplicacao):
        self.vc.dump()
         
        resultado = float(self.vc.findViewWithAttribute("content-desc","result").getText())
         
        return resultado == multiplicacao
    
        
    def checar_titulo(self):
        titulo = self.vc.findViewWithText("AndroidCalculator")
        return titulo != None
    
    def limpar_campo(self,campo):
        campo.touch()
        for b in range(10):
            self.device.press("DEL",self.device.DOWN_AND_UP)
    
        
    def fechando_calculadora(self):
        if self.checar_titulo != None:
            self.device.press("KEYCODE_BACK", self.device.DOWN_AND_UP)
        else:        
            self.util.trocar_aplicacao("AndroidCalculator")
            self.vc.dump()
            self.device.press("KEYCODE_BACK", self.device.DOWN_AND_UP)
        
    
        
