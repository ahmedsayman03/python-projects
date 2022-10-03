'''
lambda is a small anonymous function. You can return a function object using
lambda.
lambda functions are single expression.

they can take arguments and do stuff with it.
'''

def mult(n):
    '''
    This takes n and returns a function that multiples anything by n

    e.g.
    mult(2) is a function that multiples any given integer by 2

    mult(3) is a function that multiples any given integer by 3
    '''
    
    # e.g. takes 2 when innit
    return lambda i: i * n
    # returns function that takes i
    # does i * 2

    # mult(2) returns a function that takes i and does i * 2

'''
Can also pass a small lambda function as an argument
'''
def new_sort(items):
    '''
    value of key is a function that takes a one argument and returns
    a key used for sorting purposes

    function runs on every list item
    '''
    # here, all items greater than two go at the end

    # less than 2 at the start
    items.sort(key = lambda i : i > 2)
    

