#Simple Game for practicing fundamentals
#Uses conditional logic, loops, and potentailly more.
# Depression Theme
import sys

def needHelp():
    print("Welcome to your free therapy session! \nLet's start with some basic questions...")
    print("How many times have you felt sad today?")
    inp = input("")
    if (int(inp) > 4 ):
        print("Damn, well its gonna get better from here.")
    
needHelp()