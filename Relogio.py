class Relogio():
    
    def __init__(self,vc,device):
        self.device = device
        self.vc = vc
                
        
             
    #Abre o relogio
    #aba - Timer ou Clock ou Stopwatch   
    def abre_relogio(self,aba):
        
        self.device.press("KEYCODE_HOME", self.device.DOWN_AND_UP)
        
        self.vc.dump()
        
        self.vc.findViewWithAttributeOrRaise("content-desc","Apps").touch()
        
        self.vc.dump()
        
        self.vc.findViewWithTextOrRaise("Clock").touch()
        
        self.vc.dump()
        
        self.vc.findViewWithAttributeOrRaise("content-desc",aba).touch()
        
        self.vc.dump()
        
        delete = self.vc.findViewWithAttributeOrRaise("content-desc","Delete")
        
        if delete != None:
            delete.touch()
            self.vc.dump(1)            
    
    
    #inicia o cronometro
    # tempo - array com o tempo para ser usado no cronometro, cada numero eh um campo
    def inicia_cronometro(self,tempo):
        
        self.abre_relogio("Timer")
        
        for b in tempo:            
            self.vc.findViewWithTextOrRaise(b).touch()
            
        
        self.vc.findViewWithTextOrRaise("Start").touch()