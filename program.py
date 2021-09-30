#the entry point of the program
#also the Root Controller 
from system import System
class Program:
    def __init__(self):
        os=System()
        System.Clear(os)
        print("Starting the Developer Console...")
if __name__== "__main__":
    Program()