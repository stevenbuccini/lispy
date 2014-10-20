from lib.aritmetic import OPERATORS

def scheme_eval(tokens):
    """Handles scheme tokens"""

    # Dealing with a standalone item.
    if type(tokens) is not list:
        # If we're dealing a lone primative, immediately return it.
        # Numbers are our only primatives for now
        if type(tokens) in [float, int]:
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

    # Placeholder for inputs like '-> 2' and '-> (2)'
    else:
        scheme_eval(token)