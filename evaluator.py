from lib.arithmetic import OPERATORS
from lispy.environment import Environment
from string import ascii_letters

def scheme_eval(tokens, env=None):
    """Handles scheme tokens"""

    # Dealing with a standalone item.
    if type(tokens) is not list:
        # If we're dealing a lone primative, immediately return it.
        # Numbers are our only primatives for now
        if type(tokens) in [float, int]:
            return tokens

        # If we're dealing with a str and it begins with a single quote,
        # it indicates a string literal so just return it as is.
        if type(tokens) is str and tokens[0] == "'":
            return tokens

        # We have a string, but not a string literal. It must resolve
        # to a variable, or error.
        if type(tokens) is str:
            return env.get(tokens)

    # We're dealing with a list, which means a new reference frame.,
    token = tokens.pop(0)

    if token in OPERATORS:
        if len(tokens) != 2:
            raise Exception("Mathematical operators require only 2 \
                            operands")
        func = OPERATORS[token]
        return func(scheme_eval(tokens[0], env),
                    scheme_eval(tokens[1], env))

    elif token == "eq?":
        if len(tokens) != 2:
            raise Exception("eq? requires only 2 arguments.")
        # TODO -- Change this to #t and #f, which is more Lisp-y
        return scheme_eval(tokens[0], env) == scheme_eval(tokens[1], env)

    elif token == 'if':
        if len(tokens) != 3:
            raise Exception("if requires truth test, true condition \
                            and false condition")
        # Must equal True exactly to avoid Python treating numbers and
        # Strings as true
        if scheme_eval(tokens[0], env) == True:
            return scheme_eval(tokens[1], env)
        elif scheme_eval(tokens[0], env) == False:
            return scheme_eval(tokens[1], env)
        else:
            raise Exception("Expression does not return a boolean.")

    elif token == 'var':
        print('adding tokens')
        var_name = tokens.pop(0)
        # First char in name must be a number to differentiate it from
        # normal numbers.
        assert(var_name[0] in ascii_letters)
        print("tokens to resolve to value", tokens[0])
        value = scheme_eval(tokens[0], env)
        env.add(var_name, value)


    # Placeholder for inputs like '-> 2' and '-> (2)'
    else:
        scheme_eval(token)
