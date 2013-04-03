class Relogio():
    '''
    Relogio page object
    '''
    def __init__(self,vc,device):
        '''
        Construtor
        
        @type vc: ViewClient
        @param vc: instancia do viewclient
        
        @type device: MonkeyDevice
        @param device: instancia do monkeyDevice 
        '''
        
        self.device = device
        self.vc = vc
                
        
        
    def abre_relogio(self,aba):
        '''
        Abre o relogio e a aba desejada
        
        @type aba: String
        @param aba: aba a ser aberta: timer, clock, stopwatch
        '''
        
        self.device.press("KEYCODE_HOME", self.device.DOWN_AND_UP)
        
        self.vc.dump()
        
        self.vc.findViewWithAttribute("content-desc","Apps").touch()
        
        self.vc.dump()
        
        self.vc.findViewWithText("Clock").touch()
        
        self.vc.dump(-1,5)
        
        self.vc.findViewWithAttribute("content-desc",aba).touch()
        
        self.vc.dump(-1,2)
        
        delete = self.vc.findViewWithAttribute("content-desc","Delete")
        
        if delete != None:
            delete.touch()
            self.vc.dump(1)            
    

    def inicia_cronometro(self,tempo):
        '''
        Inicia o cronometro
        
        @type tempo: array
        @param tempo: array com o tempo para ser usado no cronometro, cada numero eh um index no array
        '''
        
        self.abre_relogio("Timer")
        
        for t in tempo:            
            self.vc.findViewWithText(t).touch()
            
        self.vc.findViewWithText("Start").touch()
        