def dict_loop():
    """Loops over sequences in different ways.

    e.g.
    Loops with index and item at the same time.

    Loops with key and value at the same time."""

    # Loop over dict
    d = {a: a*2 for a in range(5)}

    # use d.items()
    # Which is: [(k, v), (k, v) etc]
    for k in d.items():
        print(k)
    # prints (k, v)

    for k, v in d.items():
        print(k, v)
    # prints k, v


def seq_loop():
    """Loops on sequence with index and item at the same time."""

    l = [i*2 for i in range(5)]

    # Use enumerate
    for i, a in enumerate(l):
        print(i, a)


def two_seq_loop():
    """Loops on 2 sequences at the same time."""

    questions = ['q', 'u', 'e']
    answers = ['a', 'n', 's']

    # Use zip
    for q, a in zip(questions, answers):
        print('Question: {0}, Answer: {1}'.format(q, a))


def seq_reverse_loop():
    """Loops over sequence in reverse."""
    l = [i * 2 for i in range(5)]

    # Use reversed()
    for i in reversed(l):
        print(i)


def sorted_loop():
    """Loops over sorted list."""
    l = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

    # Use sorted()
    # It creates a new list, l is unchanged.

    # Uses set() because set removes repeats.
    # So, for example, 'apple' won't print twice.
    for i in sorted(set(l)):
        print(i)


def change_list_loop():
    """Creates new list instead of changing over a list that is being looped over.

    Shows what to do instead of changing a list that you are looping on (not a good idea)."""
    r = [i*2 for i in range(5)]
    filtered_r = []
    for i in r:
        if i == 4:
            filtered_r.append(i)  # append to new list

    print(filtered_r)
    # This way, the list being looped on never changes.


