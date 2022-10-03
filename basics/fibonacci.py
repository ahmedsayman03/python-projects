def fib():
    '''
    The fibonacci sequence is such that each new number
    is the sum of the two previous numbers.
    The first two numbers are 0 and 1.
    
    e.g. 0, 1, 1, 2, 3, 5, 8, 13
    '''
    x = 0
    y = 1
    i = 0 # incrementing counter
    
    print(x, end = ' ')
    print(y, end = ' ')
    while i < 10: # 10 fib numbers after 0 and 1
        n = x + y
        
        print(n, end = ' ')

        x = y 
        y = n
        i += 1

fib()
        
        
    
