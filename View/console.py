#console commands
import sys
import os
class Console:
	@staticmethod #this method clear the terminal
	def Clear():
		#get the right command
		# windows
		if sys.platform.startswith('win32'):
			os_cmd='cls'
		# linux and OS X
		elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
			os_cmd='clear'
		else:
			raise Exception('System Error: Unknown operating system')
		try:
			if os.system(os_cmd) != 0:
				msg='System Error: Wrong operating system command'
				raise Exception(msg)
		except:
			raise Exception(f"Fatal Error!\n Reason:\n{msg}")