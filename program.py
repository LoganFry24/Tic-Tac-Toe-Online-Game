#the entry point of the program
#also the Root Controller 
from Controller.system import System
from Controller.config import Config
import pygame
import sys
class Program():
	game="Tic-Tac-Toe Online Game"
	def __init__(self):
		#System Check
		print("Checking the system...")
		self.os=System()
		System.Clear()
		print("System is checked")
		print("Starting the Developer Console...")
		#check the window configuration
		c=Config()
		#Window()
		screen = pygame.display.set_mode((600, 600))
		pygame.display.set_caption('TIC TAC TOE')
		
	def __str__(self):
		return "Tic-Tac-Toe Online Game"
	def __repr__(self):
		return f"Program[\nOperating System: {self.os}\nGame Title: {self.game}\n]"
	def __del__(self):
		print("Developer Console:")
		print("Program stopped")

#if you compile this file, start the program
if __name__== "__main__":
	# thats how you can invite the whole game in your program
	game=Program()

#FOR DEV PURPOSE
# this commands are dev tools for you to get informations about the program
print(game) # the print out the name of the program using the __str__() function
print(repr(game)) # representation of the main Program's object using the __repr__() function