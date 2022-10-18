def packages():
    """Structures python's module namespace using dot notation (dotted module names). It's a collection of modules."""

    # A.B
    # B is a sub module in package A

    # Suppose a module has variables
    # Another module has variables
    # mod.var
    # anothermod.var
    # Dot notation good because now modules don't have to worry about another modules variable names.

    # Similarly
    # Multi-module packages don't have to worry about other package's module names.

    # Package: Collection of modules

    # e.g.
    # sound /
    #   __init__.py can be empty, or exectue initializaiton code for package. Used to show python it is a package.
    #               Initialize the sound package
    #
    #   format /
    #       __init__.py Tells python that directories containing this file are treated as packages.
    #                   Subpackage for file formats. ALl files below are modules.
    #       mp3.py
    #       aiff.py
    #       wav.py
    #   effects /
    #       __init__.py Subpackage for sound effects.
    #       echo.py
    #       surround.py
    #
    #   filters /
    #       __init__.py Subpackage for filters
    #       karaoke.py
    #       equalizer.py

    # Package users can import individual modules:
    # import sound.effects.echo
    # Reference full name needed:
    # sound.effects.echo.echolfilter()

    # sound.effects.echo in symtable, not it's functions

    # from sound.effects import echo
    # echo.echolfilter()
    # echo in symtable now

    # from sound.effects.echo import echofilter()
    # echofilter()
    # Function echofilter() directly available as it is in the symtable

    # Note:
    # from package import item
    # This syntax imports names (item) in package, if not it tries to load the module

    # i.e.
    # searches package for name item (function, variable, class etc.)
    # If not found, it assumes it's a module in the package and loads it

    # Cannot find that either? Raises ImportError

    # Contrary
    # import i.s.subs
    # This syntax only imports modules / packages

    # i.e.
    # i.s need to both be packages
    # subs needs to be a module or package
    # Cannot be a class, function, name defined in previous module or package
    pass
