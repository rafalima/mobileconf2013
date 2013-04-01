#define configuracoes do ambiente
def ambiente():        
    arquivo_apk="/home/tworker/workspace/monkeyrunner/apk/Main.apk"
    
    configs = {'arquivo_apk':arquivo_apk}
    
    return configs


#responsavel por colocar o android view client no path
def importar():
    import sys
    import os
    
    # this must be imported before MonkeyRunner and MonkeyDevice,
    # otherwise the import fails
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

