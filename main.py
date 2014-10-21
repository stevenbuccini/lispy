from lib.helpers import clear_screen
from parser import parse
from evaluator import scheme_eval

def main():
    clear_screen()
    while True:
        response = input('> ')
        tokens = parse(response)
        print(tokens)
        result = scheme_eval(tokens)
        print('=> ' + str(result))

if __name__ == '__main__':
    main()