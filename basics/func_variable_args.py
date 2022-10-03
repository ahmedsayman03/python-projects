# one function, multiple ways to call

# with different argument numbers

def ask_ok(prompt, retries=4, reminder='Please try again!'):
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


# function above can be called three ways:

# ask_ok('Do you want to quit?')

# ask_ok('Do you want to quit?', 2)

# ask_ok('Do you want to quit?', 2, 'Incorrect input, try again')

'''
Note: default value only assigned once.

def f(a, L=[]):
    L.append(a)
    print(L)
    return L

f(1)
f(2)
f(3)

L is
[1, 2, 3]

If you want default value to change:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    print(L)
    return L

f(1)
f(2)
f(3)

L is
[3]
'''

