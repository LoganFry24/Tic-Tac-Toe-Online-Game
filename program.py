#the entry point of the program
#also the Root Controller 
from Controller.system import System
from Controller.config import Config
import sys
class Program():
	#constants
	game="Tic-Tac-Toe Online Game"
	#build and tested on
	python="3.8.10"
	pyg="2.0.1"
	#constructor
	def __init__(self,devmode):
		self.devmode=devmode
		#System Check
		print("Checking the system...")
		self.os=System.Check()
		System(devmode,self.python,self.pyg)
		#system.CheckPygame()
		
		#startup the console
		#system.Startup()
		#check the window configuration
		#c=Config()
		#Window()
		#screen = pygame.display.set_mode((600, 600))
		#pygame.display.set_caption('TIC TAC TOE')
	def __str__(self):
		return "Tic-Tac-Toe Online Game"
	def __repr__(self):
		return f"Program[\nOperating System: {self.os}\nGame Title: {self.game}\nPython version: {self.python}\nPygame version: {self.pyg}\nDeveloper mode: {self.devmode}]"
	def __del__(self):
		print("Developer Console:")
		print("Program stopped")

#if you compile this file, then start the program
if __name__== "__main__":
	# that's how you can invite the whole game in your program
	devmod=True # you should disable the dev mode before you build the program
	game=Program(devmod)
	input()
	
#FOR DEV PURPOSE
#If you want to use my game as a module in your program then
# you can use these commands to get informations about the program
print(game) # the print out the name of the program using the __str__() function
print(repr(game)) # representation of the main Program's object using the __repr__() function