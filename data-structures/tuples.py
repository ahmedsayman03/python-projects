def tuples():
    """Uses tuples (standard sequence data type).

    Sequence data types are like lists and strings. They share common properties (e.g. indexing, slicing)."""

    t = 123, 456, 'hello'

    # Index
    print(t[0])
    print(t)

    # Nested
    u = t, (1, 2, 3, 4)

    print(u)

    # Not mutable
    # But can contain mutable objects
    l = ([1, 2, 3], 4, '5')
    l[0][0] = 80

    # Tuples: immutable, normally heterogeneous, accessed via unpacking or indexing, or attribute in case of named
    # tuples.
    # Lists: mutable, homogeneous, accessed via iterating over the list.

    empty_tuple = ()

    # Need comma after single tuple
    singleton = (1,)


def tuple_packing():
    """Packs and unpacks tuples."""

    # Example of tuple packing:
    # The values 123, 456, '7' are packed together in a tuple.
    t = 123, 546, '7'

    # Reverse
    # Sequence unpacking (any sequence can be on RHS):
    x, y, z = t

    # LHS variables == number of elements in sequence


