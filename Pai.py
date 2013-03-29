import unittest

# this must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails
from com.dtmilano.android.viewclient import ViewClient, View

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
 
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
            print"Device found..."    
        self.runAndroidCalculator()
        
    def tearDown(self):
        pass
#         self.runAndroidCalculator()
#         self.device.press("KEYCODE_BACK", self.device.DOWN_AND_UP)
#         
        
        
    def runAndroidCalculator(self):
        
        apk_path = self.device.shell('pm path com.calculator')
        if apk_path.startswith('package:'):
            print "myapp already installed."
        else:
            print "myapp not installed, installing APKs..."
            self.device.installPackage('/Users/rlima/Documents/workspace/eclipse/MRTest/apk/Main.apk')
        
        print "launching myapp..."
        self.device.startActivity(component='com.calculator/.Main')
        
        self.vc = ViewClient(self.device,serialno=self.serialno)