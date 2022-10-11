def dir_f():
    """The dir function lists names, variables, functions and modules defined (currently or in a module)."""

    dir()  # Currently defined names

    # import fibo
    # dir(fibo)
    # Lists names, variables, functions, modules etc. in fibo

    # import fibo
    # a = []
    # fib = fibo.fib
    dir()  # Lists 'a', 'fib', 'fibo'
    # i.e. your sym table!
    # Notice fib is there and so is fibo
    # It's your files sym table

    # To list built-in names, do this:
    # import builtins
    # dir(builtins)
    # Lists builtin functions, variables etc.
    # e.g.
    # len, map, enumerate, dict
    pass
