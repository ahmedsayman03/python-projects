def arb_args(first, *arguments):
    """Takes multiple arguments.

    e.g.
    arb_args(1, 2, 3, 4)

    arb_args(1, 2, '3', '4')
        Can be strings or ints

    arb_args(1, 2, 3, first=4)
        Raises Error
        TypeError: got multiple values for argument 'first'
        Mandatory arguments have to come first, otherwise it will be as if you are giving multiple values for first
        argument.

    arb_args(first=1, 2, 3)
        Raises Error
        SyntaxError: positional argument follows keyword argument
        The above is seen as a kwarg, and the positional first argument is 2. Positional argument = mandatory arguments.

    Cannot take kwargs since **kwargs is not a parameter.
    """

    print(first)
    print('-' * 40)

    for arg in arguments:
        print(arg)


def arb_kwargs(first, *arguments, **kwargs):
    """Takes multiple keyword arguments (dictionaries).

    e.g.
    arb_kwargs(second=2, third=3, first=1)

    arb_kwargs(1, second=2, third='3')
        Type of parameters is string, but the value of them remains the same type.
        2 is an int, 3 is a str.

        e.g. For second
        type(kw) -> String #  second
        type(kwargs[kw]) -> int #  2

    arb_kwargs(second=2, 1)
        Raises Error
        kwargs always come after positional arguments.
    """
    print(first)
    print('-' * 40)

    for arg in arguments:
        print(arg)

    print('-' * 40)

    for kw in kwargs:
        print(kw, ':', kwargs[kw])


def test_sep(*args, sep='/'):
    """Takes arbitrary args and separates them with the kwarg at the end."""

    #  args has to be strings since join only takes strings
    print(sep.join(args))



