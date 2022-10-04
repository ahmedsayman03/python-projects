
def finding_even_odd_continue():
    """Prints if first 10 numbers are even or odd. Uses continue."""

    for i in range (1, 10):
        if i % 2 == 0:
            print(i, 'Even')
            continue

        #  Could remove continue and replace with an else here
        print(i, 'Odd')


finding_even_odd_continue()
