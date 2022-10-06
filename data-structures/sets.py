def sets():
    """Prints the various math operations for sets (Similar to sets and collections learned in algebra).

    e.g.
    a = {'123'}
    b = {'345'}

    Sets can show what's in both a and b, what's shared, what's not shared.

    Note: Sets are not ordered."""

    a = set('abcdefaah')
    b = set('abcdefddg')
    
    print(a)
    print(b)
    print(a - b)  # a not b,      in a, not in b
    print(a | b)  # all,          in a, in b, in both
    print(a & b)  # shared,       both in a and b
    print(a ^ b)  # not shared,   in a, in b, not in both


def set_com():
    """Prints set comprehension."""
    a = {x for x in 'abcd' if x not in 'ab'}
    print(a)


