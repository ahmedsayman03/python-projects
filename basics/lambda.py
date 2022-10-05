def mult(n):
    """Returns a function that multiples int by n.

    Lambda is a small anonymous function.
    You can return a function object using lambda.
    Lambda functions are single expressions.
    They can take arguments and do stuff.

    e.g.
    mult(2)
        returns function that multiplies by 2.

    mult(3)
        returns function that multiples by 3.
    """

    return lambda x: x*n


def new_sort(items):
    """Passes lambda function as an argument.

    Sorts items based on key: if they are greater than 2 or not.

    e.g.
    new_sort([4,3,2,1,6,8])
        returns [2, 1, 4, 3, 6, 8]
    """

    #  Value of key is a function that takes one argument and returns a key used for sorting items in items.
    #  All items greater than 2 go at the end.
    items.sort(key=lambda x: x > 2)
    print(items)
