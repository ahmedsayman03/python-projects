def dc(values):
    """Splits list of values into half, and calls merge() recursively."""
    if len(values) == 1:  # If it's in the atomic state, e.g. [1], don't split, merge them
        return values

    else:
        half = len(values) // 2
        # Split the list in half, and keep recursively splitting until atomic state, then recursively merge them back
        return merge(dc(values[:half]), dc(values[half:]))


def merge(v1, v2):
    """Merges two lists into one list (that is in ascending order).

    Pseudocode:
    Compare each item in list 2 to list 1
    if item in list 2 is less than item in list 1, insert the item into list 1 in the appropriate spot
    If it reaches the end of list 1 (i.e. item 2 is greater than all items in list 1), then append the rest of list 2
    into list 1, as all remaining items in list 2 are greater than list 2

    The code below uses 2 for loops.
    It can be done more efficiently with while statements:

    while list1 and list2:
        if list1[0] < list2[0]
            insert list1 item into list 3, remove list1[0]
        else
            insert list2 item into list 3, remove list2[0]

    while list1:
        put all list 1 items into list 3

    while list2:
        put all list 2 items into list 3
    """
    done = False

    # Compare all list 2 items to list 1
    for v2_index, v2_int in enumerate(v2):
        if done:
            break

        for v1_index, v1_int in enumerate(v1):
            # place list 2 items into list 1 appropriately
            if v2_int < v1_int:
                v1.insert(v1_index, v2_int)
                break

            # If it reaches the end of list 1, put all list 2 items at the end of list 2, as all remaining list 2
            # items are greater than list 1
            elif v1_index == len(v1) - 1:
                v1.extend(v2[v2_index:])
                # No longer need to go through the rest of list 2 as we know they all are greater than list 1
                done = True
                break

    return v1


print(dc([1, 5, 2, 3, 4, 6, 8, 7]))
