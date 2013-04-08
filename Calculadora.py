import Config
from Util import Util


class Calculadora():    
    '''
    Calculadora Page Object
    '''
    
    def __init__(self, vc, device):
        '''
        Construtor
        
        @type vc: ViewClient
        @param vc: instancia do viewclient
        
        @type device: MonkeyDevice
        @param device: instancia do monkeyDevice 
        '''
        
        self.vc = vc
        self.device = device
        self.util = Util(self.device,self.vc)
                            
            
    def inicia_calculadora(self):
        '''
        Inicia a calculadora
        '''
        
        self.device.press("KEYCODE_HOME", self.device.DOWN_AND_UP)
        
        self.vc.dump()
        
        self.vc.findViewWithAttribute("content-desc","Apps").touch()
        
        self.vc.dump()
        
        self.vc.findViewWithText("AndroidCalculator").touch()
        
        self.vc.dump()
        
    
    def multiplicacao(self,primeiro,segundo):
        '''
        Executa uma multiplicacao
        
        @type primeiro: float
        @param primeiro: numero a ser inserido no primeiro campo
        
        @type segundo: float
        @param segundo: numero a ser inserido no segundo campo
        
        @return: Retorna o resultado da multiplicacao
        '''
        
        
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
        '''
        Checa se o resultado da multiplicacao eh igual ao da aplicacao
        
        @type multiplicacao: float
        @param multiplicacao: multiplicacao entre os dois numeros inseridos na aplicacao
        
        @return: Retorna bool para a checagem do resultado  
        '''
        
        self.vc.dump()
         
        resultado = float(self.vc.findViewWithAttribute("content-desc","result").getText())
         
        return resultado == multiplicacao
    
        
    def checar_titulo(self):
        '''
        Checa se a aplicacao esta sendo mostrada
        
        @return: Retorna bool para a checagem do resultado
        '''
        
        titulo = self.vc.findViewWithText("AndroidCalculator")
        return titulo != None
    
    def limpar_campo(self,campo):
        '''
        Limpa um campo antes da insercao
        
        @type campo: View
        @param campo: view do campo a ser limpado 
        '''
        campo.touch()
        for b in range(10):
            self.device.press("DEL",self.device.DOWN_AND_UP)
    
        
    def fechando_calculadora(self):
        '''
        Fecha a calculadora
        '''
        if self.checar_titulo != None:
            self.device.press("KEYCODE_BACK", self.device.DOWN_AND_UP)
        else:        
            self.util.trocar_aplicacao("AndroidCalculator")
            self.vc.dump()
            self.device.press("KEYCODE_BACK", self.device.DOWN_AND_UP)
        
    
        
