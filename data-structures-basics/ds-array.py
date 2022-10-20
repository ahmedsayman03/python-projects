"""Arrays:
    [ items ]
    type == same

Most DS use arrays for operations / algorithm implementations

element - i stored in array
index - element's numerical index

e.g.
    int array [10] = {1, 2, ..., 10}
    type name size

    [1 2 .... 10]
    size: 10 (stores 10)

    0 index 0 start

    element accessed via index


OPS
traverse, insert, delete, search, update elem @ index

init array w size

bool array [false, false, false]
                 size: size

OR

int array [0 0 0 0]
            size: size

default vals init

E.g."""


def traverse(ar):
    """Traverse and print elems in array."""
    for index, i in enumerate(ar):
        print('AR[{}] = {}'.format(index, i))


def insert(ar, item, ind):
    """Insert item into array ar at index ind."""
    # Initialize new array of length ar + 1 (+ 1 for the inserted item)
    new = [0 for i in range(len(ar) + 1)]

    # variable that changes to 1 after item is inserted
    space = 0

    for index, i in enumerate(ar):
        if index == ind:
            new[index] = item
            # From now on, insert all items in ar into new but 1 space to the right, since the inserted item
            # is taking up a spot
            space = 1

        new[index + space] = i

    print(new)


def delete(ar, ind):
    """Delete item at index ind in array ar."""
    # New array will be 1 item less than original (after deletion)
    size = len(ar) - 1
    new = [0 for item in range(size)]

    i = 0

    space = 0

    # size + 1 because new array is 1 smaller than original, but we want to loop through original
    while i < size + 1:
        if i != ind:
            # put array item into new item
            new[i - space] = ar[i]

        else:
            # Remove

            # From now on, place item in position x in array into position x-1 in new array (handles deleted item)
            space = 1

        i = i + 1

    print(new)


def search(ar, item):
    """Searches array for a given item."""
    found = False
    for index, i in enumerate(ar):
        if i == item:
            print('Found item {} at position {}'.format(item, index))
            found = True
            break

    if not found:
        print('Item not in array')


search([1, 3, 5, 7, 9], 4)
