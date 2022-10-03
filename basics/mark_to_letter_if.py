def mark_to_letter_if(mark):
    '''
    (int) -> str
    takes a mark 0-100
    returns this

    0-50 F
    50-60 D
    60-70 C
    70-80 B
    80-90 A
    90-100 A+
    '''
    if mark < 0 or mark > 100:
        return 'Inncorrect input'
    
    elif mark < 50:
        return 'F'

    elif mark < 60:
        return 'D'

    elif mark < 70:
        return 'C'

    elif mark < 80:
        return 'B'

    elif mark < 90:
        return 'A'

    else:
        return 'A+'
