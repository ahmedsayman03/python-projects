def list_del():
    """Deletes from a list based on index, without returning a value.

    Also deletes slices."""

    l = [i for i in range(10)]

    # Doesn't return anything
    del l[2]

    # Delete slices
    del l[2:6]

    del l[:]

    # Delete entire variables
    del l

    # Can no  longer reference l
