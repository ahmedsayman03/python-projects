def import_all():
    """Importing * from packages does not import all sub modules (only Package and names)."""

    # When doing
    # from package import *
    # Python checks in the __init__ if it has an
    # __all__ = ["echo", "surround", "reverse"]
    # and imports those modules.

    # If no all, imports package and all it's names. It does NOT import submodules.

    # from package import sub_module
    # Above is good, use it.

    # Using import * is not good.
    pass
