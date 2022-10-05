# one function, multiple ways to call

# with different argument numbers

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """Demonstrates calling function in multiple different ways.

    e.g. Can be called four ways
    ask_ok('?')

    ask_ok('?', 2)

    ask_ok('?', 2, 'Come again?')

    ask_ok('?', reminder='Come again?', retries=2)

    ask_ok(reminder='Come again?', retries=2, '?')
        Raises Error
        Positional arguments cannot come after kwargs.
    """
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# Note: default value only assigned once.
#
# def f(a, L=[]):
#     L.append(a)
#     print(L)
#     return L
#
# f(1)
# f(2)
# f(3)
#
# L is
# [1, 2, 3]
#
# If you want default value to change:
# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     print(L)
#     return L
#
# f(1)
# f(2)
# f(3)
#
# L is
# [3]
