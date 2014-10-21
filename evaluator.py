from lib.arithmetic import OPERATORS

def scheme_eval(tokens):
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

        # TODO: Handle support for variables.

    # We're dealing with a list, which means a new reference frame.,
    token = tokens.pop(0)

    if token in OPERATORS:
        if len(tokens) != 2:
            raise Exception("Mathematical operators require only 2 \
                            operands")
        func = OPERATORS[token]
        return func(scheme_eval(tokens[0]),
                    scheme_eval(tokens[1]))

    if token == "eq?":
        if len(tokens) != 2:
            raise Exception("eq? requires only 2 arguments.")
        # TODO -- Change this to #t and #f, which is more Lisp-y
        return scheme_eval(tokens[0]) == scheme_eval(tokens[1])


    # Placeholder for inputs like '-> 2' and '-> (2)'
    else:
        scheme_eval(token)