#this class check the whole system
import sys
from View.console import Console
class System:
	# get the name of the operating system
	@staticmethod
	def Check():
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
			raise Exception('System Error: Unknown operating system')
		return os
	#constructor
	def __init__(self,devmode,python,pyg):
		self.devmode=devmode
		self.python=python
		self.pyg=pyg
		self.CheckColor()
	#check colorama
	def CheckColor(self):
		try:
			import colorama
			from colorama import Fore as color, Style as style
			colorama.init(autoreset=True)
		except:
			raise Exception("valami")
		self.CheckPygame(color)
	# check the installed pygame
	def CheckPygame(self,color):
		try:
			import pygame as py
			self.Startup(py)
		except:
			a=color.RED+"Pygame version: Pygame is not installed on your system"
			b=color.YELLOW+"If you want to compile or build this program, you have to install the pygame!"
			c="To install pygame use this command: pip install pygame"
			raise Exception(f"{a}\n{b}\n{c}")
	# check you own system and compare with the original
	def Startup(self,py):
		Console.Clear()
		print ("Operating System is checked")
		if self.devmode== True:
			self.GetVersion(py)
		print("Program build and tested on:")
		print(f"Python version: {self.python}")
		print(f"Pygame version: {self.pyg}")
		print("System is checked")
		print("Starting the Developer Console...")
	def GetVersion(self,py):
		print("Your configuration:")
		print(f"Python version: {sys.version}")
		print(f"Pygame version: {py.__version__}")
	def __del__(self):
		pass