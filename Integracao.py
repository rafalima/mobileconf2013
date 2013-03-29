from Pai import Pai

class Integracao():
    
    def __init__(self,vc,device):
        self.vc = vc
        self.device = device
        
        
        
    def calculadora_cronometro(self,multiplicacao):
        
        self.device.press("KEYCODE_HOME",self.device.DOWN_AND_UP)
         
        self.vc.dump(1)
         
        self.vc.findViewWithAttributeOrRaise("content-desc","Apps").touch()
         
        self.vc.dump()
         
        self.vc.findViewWithTextOrRaise("Clock").touch()
         
        self.vc.dump()
         
        self.vc.findViewWithAttributeOrRaise("content-desc","Timer").touch()
        
        self.vc.dump()
        
        delete = self.vc.findViewWithAttributeOrRaise("content-desc","Delete")
        
        if delete != None:
            delete.touch()
            self.vc.dump(1)
            
        
        self.vc.findViewWithTextOrRaise("5").touch()
        
        self.vc.dump(1)
        
        self.vc.findViewWithTextOrRaise("1").touch()
        
        
        self.vc.findViewWithTextOrRaise("Start").touch()
        
        self.runAndroidCalculator()
        
        self.vc.dump()
        
        resultado = self.vc.findViewWithAttributeOrRaise("content-desc","result").getText()
        
        self.assertEqual(float(resultado),multiplicacao)
        
        self.vc.dump(60)
    