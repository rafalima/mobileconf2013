import unittest
# this must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails
from com.dtmilano.android.viewclient import ViewClient, View

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import Config
 
class Pai(unittest.TestCase):
      
#     @classmethod
#     def setUpClass(self):
#         self.device = MonkeyRunner.waitForConnection()
#         self.device.wake()
#         if self.device != None:
#             print"Device found..."
        
       
    def setUp(self):
        self.serialno = "emulator-5554"
        self.device = MonkeyRunner.waitForConnection()
        self.device.wake()
        if self.device != None:
            print "Dispositivo encontrado..."    
        self.instala_calculadora()
        self.vc = ViewClient(self.device,serialno=self.serialno)
        
    def tearDown(self):
        pass      
        
        
    def instala_calculadora(self):
        caminho_apk = self.device.shell('pm path com.calculator')
        if caminho_apk.startswith('package:'):
            print "calculadora instalada."
        else:
            print "calculadora nao instalada, instalando..."
            configs = Config.ambiente()
            self.device.installPackage(configs['arquivo_apk'])
