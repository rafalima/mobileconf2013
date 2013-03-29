class Util():
    
    def __init__(self,device,vc):
        self.device = device
        self.vc = vc
    
    
    def trocar_aplicacao(self,aplicacao):
        self.device.press('KEYCODE_APP_SWITCH', self.device.DOWN_AND_UP)
        self.vc.dump(1)
        self.vc.findViewWithTextOrRaise(aplicacao).touch()
        
        