
def finding_even_odd_continue():
    '''
    numbers from 1 to 10, not including 10, even or odd?

    uses continue
    '''
    for i in range(1, 10):
        if i % 2 == 0:
            print(i, 'even')
            continue
        # could remove the continue above and put else here
        print(i, 'odd')

finding_even_odd_continue()
