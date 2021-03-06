class Util():
    '''
    Classe com metodos utilitarios para todos os testes
    '''
    
    def __init__(self,device,vc):
        '''
        Construtor        
        
        @type device: MonkeyDevice
        @param device: instancia do monkeyDevice
        
        @type vc: ViewClient
        @param vc: instancia do viewclient
         
        '''
        
        self.device = device
        self.vc = vc
    

    def trocar_aplicacao(self,aplicacao):
        '''
        Responsavel por trocas as aplicacoes
        
        @type aplicacao: String
        @param aplicacao: nome da aplicacao a ser chamada 
        '''
        
        self.device.press('KEYCODE_APP_SWITCH', self.device.DOWN_AND_UP)
        self.vc.dump()
        self.vc.findViewWithText(aplicacao).touch()
        

    def instala_calculadora(self):
        '''
        Instala a calculadora caso ja nao esteja instalada
        '''
        
        caminho_apk = self.device.shell('pm path com.calculator')
        if caminho_apk.startswith('package:'):
            print "calculadora instalada."
        else:
            print "calculadora nao instalada, instalando..."
            configs = Config.ambiente()
            self.device.installPackage(configs['arquivo_apk'])

        
        
        
        