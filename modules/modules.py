def modules():
    """Creates modules with a fibonacci function.

    With modules, interpreter reads file as input (this is called a script).

    Also, nice to break down long programs into smaller files, it is easier.

    Also, if you want one handy function used in multiple files and don't want to copy / paste it,
    modules are helpful.

    A module file has definitions and statements. Can be used in a script or an interactive interpreter.
    Can import it into another module file as well.

    The file name is the module name with the .py suffix."""
    pass


def fibo():
    """Prints fibonacci numbers: a number that is the sum of the two previous numbers, starting with 0 and 1.

    e.g.
    0 1 1 2 3 5 8 13"""

    f = 0
    s = 1

    for i in range(10):
        print(f)
        n = f + s
        f = s
        s = n


# Now we open interpreter and import(modules).
# The interpreters Sym Table will have modules, not the functions.
# Do modules.fibo() to access the functions.
# If you intended to use module function often, you can do
# f = modules.fibo
