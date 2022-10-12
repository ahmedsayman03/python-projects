def strings():
    """Multiple ways to print strings with variables."""

    year = 2022
    # Use variables in string with f and {}
    print(f'It is the year {year}')

    # Can make it an expression too when using f
    print(f'It is the year {2020 + 2:10d}')
    # :10d makes it minimum 10 spaces. Good for spacing out strings to make it more readable.

    # Use variables in strings with {0} and .format()
    print("It is the year {}".format('2022'))

    # Can use positional kwargs as well with format
    print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

    # str()
    # Converts anything into a string.
    s = str([i for i in range(5)])

    print(s)


strings()
