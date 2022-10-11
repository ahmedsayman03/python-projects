def scripts():
    """Explains how to use a module as a script (using __name__=='__main__' to run from shell / command line)."""

    # You can run modules as a script, from the shell / command line:
    # python fibo.py args
    # Similar to importing, but:
    # __name__ == "__main__"

    # So add this to module file (for it to run as script instead of just a module to import):

    # if __name__ == "__main__":
    #     import sys
    #     fib(int(sys.argv[1]))

    # Now, if I just import it like so
    # import fibo
    # The code above will not run since importing a module does not make __name__ = __main__
    pass