def squares():
    """Prints the squares from 0-10"""

    print([x**2 for x in range(10)])

    print('-'*40)

    # Above is better than below:
    my_squares = []
    for y in range(10):
        my_squares.append(y**2)
    print(my_squares)
    # Since y is created and overwritten and still remains after the loop.

    print('-' * 40)

    # Comprehension is equivalent to the map function:
    # map(func, *iterables)
    print(map(lambda x: x**2, range(10)))
    # Essentially, takes whatever is in the iterables, and places them through the lambda function.


def same():
    """Takes two lists, and prints the tuples (x in first list, y in second list) iff x is not y.

    e.g.
    [3,2], [1,2] -> [(3,1), (3,2), (2,1)]"""

    print([(x, y) for x in [3, 2] for y in [1, 2] if x != y])

    # Closest lambda map to above is this:
    # print(list(map(lambda x, y: (x, y) if x != y else None, [3, 2], [1, 2])))
    # But you cannot use for loops in lambda, so use list comprehension
    print('-'*40)

    # Without comprehensions, this is how it is done:
    x = [3, 2]
    y = [1, 2]
    diff = []
    for x_i in x:
        for y_i in y:
            if x_i is not y_i:
                diff.append((x_i, y_i))
    print(diff)
    # Clearly, when doing a bunch of for / if's then returning a list, list comprehension is much more efficient.


def exact_same():
    """Prints list of tuples such that integers at i are the same in list x and list y.

    e.g.
    x = [1, 2, 3]
    y = [4, 2, 6]
        prints (2, 2)"""
    x = [1, 2, 3]
    y = [4, 2, 6]
    es = []

    # print([(x[i], y[i]), [1, 2, 3], [4, 2, 6], for i in range(3) if x[i] is y[i]])
    # The above does not work because you cannot create lists inside comprehension,
    # so create x and y lists before comprehension.
    print([(x[i], y[i]) for i in range(3) if x[i] is y[i]])

    for i in range(3):
        if x[i] == y[i]:
            es.append((x[i], y[i]))
    print(es)


exact_same()
