def comp_seq():
    """Compares sequences (lists, strings, integers)."""

    print((1, 2, 3) < (1, 2, 4))  # index i in first seq compared to index i in second seq. True
    print([1, 2, 3] < [1, 2, 4])  # True
    print('ABC' < 'C' < 'Pascal' < 'Python')  # True. A comes before C. C before P. Pa comes before Py.
    print((1, 2, 3, 4) < (1, 2, 4))  # 3 < 4. True
    print((1, 2) < (1, 2, -1))  # integers same, longer length is greater
    print((1, 2, 3) == (1.0, 2.0, 3.0))  # True
    print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))  # aa comes before ab. True

    print('b' < 'b')  # False
    print('bc' < 'bca')  # Longer length is greater. True
    print('bc' < 'bc') # False


