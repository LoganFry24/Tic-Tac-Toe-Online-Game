#this class check the whole system and the required modules
import sys
from View.console import Console
class System:
	# get the name of the operating system
	def CheckOS(self):
		# windsows
		if sys.platform.startswith('win32'):
			os='Windows'
		# linux 
		elif sys.platform.startswith('linux'):
			os='Linux'
		#OS X
		elif sys.platform.startswith('darwin'):
			os='Mac'
		else:
			raise Exception(self.color.RED+'System Error: Unknown operating system')
		print(self.color.GREEN+"Operating System is checked"+self.color.RESET)
		#os=self.CheckOS(self)
		self.su=self.Version()
		return os
	#constructor
	def __init__(self,devmode,python,pyg):
		self.devmode=devmode
		self.python=python
		self.pyg=pyg
		self.su=False
		self.CheckModules()
	def CheckModules(self):
		#check colorama
		self.color=self.CheckColor()
		#check the pygame
		self.py=self.CheckPygame()
		Console.Clear()
		print(self.color.GREEN+"Python modules checked"+self.color.RESET)
	#check colorama
	def CheckColor(self):
		try:
			import colorama
			from colorama import Fore as color
			colorama.init(autoreset=True)
		except:
			a="Colorama is not installed."
			b="If you want to compile or build this program, you have to install colorama."
			c="To install colorama use this command: pip install colorama"
			raise Exception(f"{a}\n{b}\n{c}")
		return color
	# check the installed pygame
	def CheckPygame(self):
		try:
			import pygame as py
		except:
			a=self.color.RED+"Pygame version: Pygame is not installed on your system"
			b=self.color.YELLOW+"If you want to compile or build this program, you have to install the pygame!"
			c="To install pygame use this command: pip install pygame"
			raise Exception(f"{a}\n{b}\n{c}")
		return py
	# check you own system and compare with the original
	def Version(self):
		if self.devmode== True:
			self.GetVersion()
		print("Program build and tested on:")
		print(f"Python version: {self.python}")
		print(f"Pygame version: {self.pyg}")
		return True
	def GetVersion(self):
		print("Your configuration:")
		print(f"Python version: {sys.version}")
		print(f"Pygame version: {self.py.__version__}")
	#destructor
	def __del__(self):
		if self.su==True:
			print(self.color.GREEN+"System is checked"+self.color.RESET)
		else:
			print(self.color.RED+"System Check has failed"+self.color.RESET)