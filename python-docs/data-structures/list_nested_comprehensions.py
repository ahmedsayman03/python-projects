def m_t():
    """Prints transpose of matrix.

    Demonstrates using lists within lists (i.e. lists within list comprehensions)

    e.g.
    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]

        prints
        [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
        ]


    """
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]

    # Do [] 4 times
    n = [[] for i in range(4)]

    for i in range(4):
        for row in matrix:
            n[i].append(row[i])
    print(n)

    # If you have trouble doing comprehensions, do it the regular way first.
    # then go from there.
    t = [[row[i] for row in matrix] for i in range(4)]
    print(t)
