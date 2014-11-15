from evaluator import scheme_eval
from lib.helpers import clear_screen
from lispy.environment import Environment
from parser import parse


def main():
    clear_screen()
    # Global environment
    env = Environment()
    while True:
        response = input('> ')
        tokens = parse(response)
        result = scheme_eval(tokens, env)
        print('=> ' + str(result))

if __name__ == '__main__':
    main()