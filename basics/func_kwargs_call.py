def parrot(first, state='state', action='action', type='type'):
    """Demonstrates when to use kwargs and position arguments at the same time.

    e.g.
    parrot()
        Raises Error
        Argument first is required.

    parrot(1, state='2')

    parrot(first=1, 's')
        Raises Error
        Positional argument cannot come after kwarg.

    parrot(guy=1)
        Raises Error
        No such argument.

    parrot(1, 's')
        Without kwargs ok since positional is provided.

    parrot(1, state='s')
        With kwargs ok since positional is provided.

    parrot(first=1, state='s')

    parrot(state='s', first=1)

    parrot(first=1, 1)
    """
    print(first)
    print(state)
    print(action)
    print(type)


