def packages():
    """Structures python's module namespace using dot notation (dotted module names). It's a collection of modules."""

    # A.B
    # B is a sub module in package A

    # Suppose a module has variables
    # Another module has variables
    # mod.var
    # anothermod.var
    # Dot notation good because not modules don't have to worry about another modules variable names.

    # Similarly
    # Multi-module packages don't have to worry about other package's module names.

    # Package: Collection of modules

    # e.g.
    # sound /
    #   __init__.py can be empty, or exectue initializaiton code for package. Used to show python it is a package.
    #
    #   format /
    #       __init__.py Tells python that directories containing this file are treated as packages.
    #       mp3.py
    #       aiff.py
    #       wav.py
    #   effects /
    #       __init__.py
    #       echo.py
    #       surround.py
    #
    #   filters /
    #       __init__.py
    #       karaoke.py
    #       equalizer.py

    pass
