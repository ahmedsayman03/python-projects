def greedy(value):
    """Definition: Closest solution that seems to provide optimum solution.

    Generally a local optimum solution, but not globally optimized solutions.

    e.g.
    Say we have 4 different types of coins: 1, 2, 5 and 10

    Problem: get value x using the least amount of coins possible.

    if x = 18
    one 10 coin, one 5 coin, one 2 coin and one 1 coin

    This works locally and is an immediate solution, but globally (say, if currency changes) it will not be the most
    efficient.

    For example, if the currency coins are just 1, 7 and 10 (instead of 1, 2, 5, 10)
    To get the value 17, this algorithm will say:
    1 10
    5 1's

    But
    2 7's
    1 1

    Is more efficient."""
    coins = []
    while value != 0:
        if value > 10:
            value = value - 10
            coins.append(10)
        elif value > 5:
            value = value - 5
            coins.append(5)
        elif value > 2:
            value = value - 2
            coins.append(2)
        else:
            value = value - 1
            coins.append(1)

    print(coins.count(10), '10')
    print(coins.count(5), '5')
    print(coins.count(2), '2')
    print(coins.count(1), '1')


greedy(18)
