def mark_to_letter_if(mark):
    """Returns letter grade of mark.

    0-50 = F
    50-60 = D
    60-70 = C
    70-80 = B
    80-90 = A
    90-100 = A+

    e.g.
    mark_to_letter_if('a')
        Runs, but raises error when it reaches the comparison str to int at
        if mark < 0 and mark > 100
    """

    if mark < 0 or mark > 100:
        print('Invalid mark')

    elif mark < 50:
        print('F')

    elif mark < 60:
        print('D')

    elif mark < 70:
        print('C')

    elif mark < 80:
        print('B')

    elif mark < 90:
        print('A')

    else:
        print('A+')
