from lib.helpers import clear_screen
from lib.primatives import PRIMATIVES
from parser import parse

def main():
    clear_screen()
    while True:
        response = input('> ')
        tokens = parse(response)
        print(tokens)

if __name__ == '__main__':
    main()