def dict():
    """Dictionary (Associative arrays).

    Indexed by keys (not numbers).
    Keys: Any immutable type (strings, numbers or tuples).
        Cannot be lists as they are mutable.

    Basically, a set of key-value pairs.
    Keys should be unique.

    Operations: Store value with key, extract with key.

    del key

    Can replace / overwrite keys.

    Error if extraction key dne.

    list(d)
        Lists all keys in insertion order.

    in
        Checks if key in dict."""

    d = {'a': 1, 'b': 2}
    d['c'] = 3

    # Note: If keys are just strings, easier to use specify pairs using keyword arguments:
    # Works in docs but gives me an error.
    # new_d = dict(a=1, b=2, c=3)
    # print(new_d)

    del d['a']

    d['a'] = 1

    print(list(d))

    # Sorts d
    print(sorted(d))

    # Use in to see if key is in dictionary or not
    print('a' in d)
    print(1 in d)


def dict_constructor():
    """Shows are dicts are built."""

    # Builds directory from a list of sequences (key-value) pairs.
    # The docs show this but I get an error.
    # dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


def dict_comprehension():
    """Creates dictionary using comprehension."""

    d = {a: a**2 for a in range(5)}
    print(d)


