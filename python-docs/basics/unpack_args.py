def unpack():
    """Unpacks list into string and dict into keys (and key value)."""
    listy = [1, 2, 3, 4, 5]
    print(*listy)
    # makes list a string, divided by spaces
    # prints
    # 1 2 3 4 5


    dicty = {'a':'hi', 'b':'bye'}
    print(*dicty)
    # prints keys, but not values

    # **dicty
    # is key and value, but hard to print
