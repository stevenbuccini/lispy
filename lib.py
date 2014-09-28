import os

def clear_screen():
    """ Clears the terminal screen. """ 
    if(os.name == "nt"):
        os.system("cls")  # clear screen for windows OS
    else:
        os.system("clear")  # unix ftw, clear their screen differently!