def ambiente():
    '''
    Local para setar as mais diversas configuracoes a serem usadas
    '''        
    
    arquivo_apk="/Users/rlima/Documents/workspace/eclipse/MobileConf/apk/Main.apk"
    
    configs = {'arquivo_apk':arquivo_apk}
    
    return configs


def importar():
    '''
    @author - Diego Milano
    Configuracao do Android View Client. Precisa ser chamado antes de importar o MonkeyRunner e o MonkeyDevice
    '''
    
    import sys
    import os
    
    try:
        for p in os.environ['PYTHONPATH'].split(':'):
            if not p in sys.path:
                sys.path.append(p)
    except:
        pass
    try:
        sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
    except:
        pass

