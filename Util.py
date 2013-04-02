class Util():
    
    def __init__(self,device,vc):
        self.device = device
        self.vc = vc
    
    #troca aplicacao
    #aplicacao - nome da aplicacao
    def trocar_aplicacao(self,aplicacao):
        self.device.press('KEYCODE_APP_SWITCH', self.device.DOWN_AND_UP)
        self.vc.dump()
        self.vc.findViewWithText(aplicacao).touch()
        
        