def fib():
    """Prints fibonacci sequence: Each number is the sum of the two previous numbers. Starting with 0 and 1.

    e.g.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    """

    f = 0
    s = 1

    for i in range(10):
        print(f, end=' ')
        n = f + s
        f = s
        s = n


fib()
