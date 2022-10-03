
def cheeseshop(kind, *arguments):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)

'''
above can take multiple arguments, like this:

cheeseshop('blue', '1', '2', '3', '4')

this is what *name does, it takes any number of arguments

**name takes any number of kwargs, e.g.

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
'''

# this takes arbitrary args, with a kwarg at the end
def test_sep(*args, sep='/'):
    print(sep.join(args))
    

test_sep('testing', 'again')
# prints testing/again
