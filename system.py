#this class check the operating system
import sys
import os
class System:
    def __new__(self):
        # windsows
        if sys.platform.startswith('win32'):
            os_cmd='cls'
        # linux and OS X
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            os_cmd='clear'
        else:
            raise Exception('System Error: Unknown operating system')
        return os_cmd
    @staticmethod #this method clear the terminal
    def Clear(os_cmd):
        try:
            if os.system(os_cmd) != 0:
                msg='System Error: Wrong operating system command'
                raise Exception(msg)
        except:
            raise Exception(f"Fatal Error!\n Reason:\n{msg}")