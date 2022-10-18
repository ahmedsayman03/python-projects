def finding_prime_for():
    """Prints if first 10 nums are prime nums or not. A prime is a num not a product of two smaller nums.

    If it is not a prime num, prints the products.
    Uses an else clause in a for loop.

    e.g.
    2 is prime
    3 is prime
    4 is 2 * 2
    5 is prime
    6 is 2 * 3
    7 is prime
    8 is 2 * 4
    9 is 3 * 3
    """

    for num in range(2, 10):
        for div in range(2, num):
            if num % div is 0:
                print(num, 'is', div, '*', num//div)
                #  Break out of innermost loop
                break

        #  If there is no break
        else:
            print(num, 'is prime')


def finding_prime_while():
    """Prints if first 10 nums are prime or not. (A num that is a product of two smaller nums)

    Prints products of num if num is not prime.
    Uses an else clause with a while loop.

    e.g.
    2 is prime
    3 is prime
    4 is 2 * 2
    5 is prime
    6 is 2 * 3
    7 is prime
    8 is 2 * 4
    9 is 3 * 3
    """

    num = 2
    while num < 10:
        div = 2
        while div < num:
            if num % div is 0:
                print(num, 'is ', div, '*', num // div)
                break
            div = div + 1

        else:
            print(num, 'is prime')

        num = num + 1


finding_prime_while()
