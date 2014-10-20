from string import whitespace
import re

def parse(user_input):
    """ Parses user input and returns a list of tokens.

    Primarily responsible for handling the different frames of the
    expression. Relies on tokenizer() to actually break the expression
    into different tokens.

    Keyword arguments:
    user_input -- String of text inputted via the command line.

    Returns a list of tokens.
    """
    # Remove beginning and trailing whitespace so the first char
    # will be a valid primative.
    user_input = user_input.strip()

    # If we see an open paren, it's the beginning of a new list.
    # Open a new frame. We look for the first closing paren due to
    # the recursive nature of frames: we work from the inside, out.
    if user_input[0] == '(':
        closing_paren = find_closing_paren(user_input)
        return parse(user_input[1:closing_paren])

    return tokenize(user_input)


def tokenize(substring):
    """ Takes a string and breaks it into tokens.

    Calls cast_to_correct_type() to convert token from a String to the
    correct primative.

    If a opening paren is found within the substring, calls parse() to
    handle the issue of framing. A token can be any non-whitespace 
    character that isn't a parenthesis.

    Keyword arguments:
    substring -- a string passed in by parse()

    Returns:
    tokens - a list of tokens, which can be primatives or itself a list
    of tokens.
    """

    tokens = []
    index = 0
    current_token = ''

    while index < len(substring):
        char = substring[index]

        # Whitespace is the delimiter for a token. Throw away the
        # the whitespace character, add the current token to the list of
        # tokens, and reset the current_token.
        if current_token and char in whitespace:
            current_token = cast_to_correct_type(current_token)
            tokens.append(current_token)
            current_token = ''
            index += 1

        # If the token is at the end of the string, it is not followed
        # by whitespace so we need to handle it in the case above.
        elif index == len(substring) - 1:
            current_token += char
            current_token = cast_to_correct_type(current_token)
            tokens.append(current_token)
            current_token = ''
            index += 1

        # If the char is an open paren, pass the rest of the substring
        # to parse() to figure out framing issues. Since parse() will
        # return a list of tokens, properly nested to represent frames,
        # we want to append the result to our list of tokens.
        elif char == '(':
            # If we were building up a token, finish it and add it to
            # the list.
            if current_token:
                tokens.append(current_token)
            closing_paren = find_closing_paren(substring)
            start = index + 1
            tokens.append(parse(substring[start:closing_paren]))
            index = closing_paren + 1

        else:
            # Only add this character if it's not a whitespace char.
            if char not in whitespace:
                current_token += char
            index += 1

    return tokens

# TODO: Should this go in helpers? It's really only helpful to this
# module.
def find_closing_paren(string_to_search):
    """ Returns the index of the last closing paren in string. 

    Raises a SyntaxError if no closing paren is found in the string.

    Keyword arguments:
    string -- the string to search for a paren.

    Returns:
    An integer representing the index of the first closing paren, or -1
    if none is found
    """
    index_of_paren = string_to_search.rfind(')')
    if index_of_paren == -1:
        # TODO: Make a badass debugger here using the knowledge
        # of the open paren at 'index' position
        raise SyntaxError('Could not find matching closing paren.')
    return index_of_paren


def cast_to_correct_type(token):
    """ Returns token cast into a type based on our best guess.

    If it's in the form (-)XX.XX, assume a number.

    Else, leave as a string.

    Keyword argument:
    token -- A string representing a single token.

    Returns:
    A primative: a number or a string.
    """
    # Test token to see if it's a number.
    pattern = re.compile('(-)?(\d)+(\.)?(\d)*')
    m = pattern.match(token)
    if m:
        if m.group(3) and m.group(4):
            # If decimal place is present, cast to float.
            return float(token)
        if m.group(3) and not m.group(4):
            # If decimal present but no numbers follow, throw an error.
            raise SyntaxError("Error parsing number: no digits " + \
                              "follow decimal point.")
        # Else, cast to int.
        return int(token)

    # Else, return String.
    return token
