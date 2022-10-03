# example of using else with a for or while loop
def finding_prime():
    '''
    Prints prime numbers (or not) until and including 9, starting from 2

    if it is not prime, print the products
    
    prime number: a number that is not a product of two (smaller) numbers,
    starting from 2
    
    Uses an else clause in a for / while loop example

    2 is prime
    3 is prime
    4 is 2 * 2
    5 is prime
    6 is 2 * 3
    7 is prime
    8 is 2 * 4
    9 is 3 * 3
    '''
    for i in range(2, 10):
        for dividing_num in range(2, i):
            if i % dividing_num == 0:
                # no remainder
                # meaning i can get divided properly

                #print(i, 'is not prime')
                #print(dividing_num, 'divides it nicely')

                print(i, 'equals', dividing_num, '*', i // dividing_num)
                break

        # executes if for loop does not break
        else:
            print(i, 'is prime')


def finding_prime_while():
    '''
    Same as above, except uses a while loop
    '''
    i = 2
    dividing_num = 2
    
    while (i<10):
        while(dividing_num < i):
            if (i % dividing_num == 0):
                print(i, 'is not prime')
                dividing_num = 2
                break
            else:
                dividing_num += 1
        else:
            dividing_num = 2
            print(i, 'is prime')
        i += 1
        
finding_prime()
    
