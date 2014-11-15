class Environment:
    """A simple wrapper for a dict that simulates an environment.
    
    Lookup is nearly identicaly to looking up an item in a dict, except
    if we can't find it in our current scope we attempt to find it in
    our parent scope, recursing up the tree until there is no parent
    scope. If that's the case, we throw an error.
    """

    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}

    def __str__(self):
        string = 'Does' if self.parent else 'Does not'
        string += 'have a parent. Vars: ' + str(self.variables)
        return string

    def add(self, name, value):
        self.variables[name] = value

    def get(self, var):
        # If we have a variable of that name in the local scope,
        # we return its value.
        if var in self.variables:
            return self.variables[var]
        # Else if we have a parent scope, we recursively call get on
        # that dictionary.
        elif self.parent:
            return self.parent.get(var)
        # If we have no parent scope and the variable isn't in the local
        # scope, throw a name error
        else:
            raise NameError("name {} is not defined.".format(var))