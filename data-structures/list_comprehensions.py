'''List comprehensions
'''

def squares():
    '''Return squares of 0-10
    '''
    squares = []
    for x in range(10):
        squares.append(x**2)
    print('Reg', squares)
    # x is created, and overwritten
    # x still remains after the loop

    # don't want x? do list comprehensions:
    squares_comp = [x**2 for x in range(10)]
    print('Comp', squares_comp)

    # equivalent, using map
    # map(func, *iterables)
    print('map', list(map(lambda x: x**2, range(10))))



def same():
    '''[list 1], [list 2] -> [same items at index]
    [3,2], [1,2] -> [(3,1), (3,2), (2,1)]
    '''
    same_reg = []
    for x in [1,2,3]:
        for y in [3,1,4]:
            if x != y:
                same_reg.append((x,y))
    print('reg', same_reg)
    
    same = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]
    print('com', same)

    print('example', [(x,y) for x in [3,2] for y in [1,2] if x != y])

def exact_same():
    x = [1,2,3]
    y = [4,2,6]
    es = []
    for i in range(3):
        if x[i] == y[i]:
            es.append((x[i], y[i]))
            
    nes = [(x[i], y[i]) for i in range(3) if x[i] == y[i]]
    print(nes)
            
    
    print(es)


