import unittest
# this must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails
from com.dtmilano.android.viewclient import ViewClient, View

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
 
class TesteBase(unittest.TestCase):
    '''
    Classe pai dos testes
    '''
          
    def setUp(self):
        '''
        Instancia o device e o vc (viewclient)
        '''
        
        self.serialno = "emulator-5554"
        self.device = MonkeyRunner.waitForConnection()
        self.device.wake()
        if self.device != None:
            print "Dispositivo encontrado..."    

        self.vc = ViewClient(self.device,serialno=self.serialno)
        
    def tearDown(self):
        pass      
