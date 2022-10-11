def imports():
    """Explains various types of imports (using import mod, from mod import f, import mod as m)."""

    # Mods can contain executable statements (that initialize the module).
    # Run when mod is imported.

    # Mods have sym table, their variables can be accessed with
    # modname.vars

    # import mod
    # Places 'mod' in sym table of this file.
    # Can now do
    # mod.function
    # mod.var

    # from mod import fib, fib2
    # The names 'fib' and 'fib2' are in the sym table now, but not 'mod'

    # from mod import *
    # Good for interactive session, bad otherwise (leads to poorly readable code, can't tell what functions are
    # being called)

    # import mod as m
    # Places 'm' in the sym table

    # from mod import fib as f
    # 'f' in sym table
    pass
