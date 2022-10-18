def del_inactive():
    """Deletes keys in dictionary if the value is 'inactive'.

    Demonstrates that you cannot delete from dictionay you are iterating over.
    Make a copy to iterate over instead."""

    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    # print("items: ", users.copy().items())
    # above line shows key, value
    # so to loop over it:
    # for key, value in users.copy().items()

    for i in users.copy():
        # i is key
        print(i)
        # users[i] is value
        print(users[i])

        if users[i] == 'inactive':
            users.pop(i)
    print(users)


def add_active():
    """Returns a dictionary of all active keys in dictionary.

    Again, don't modify dictionary you are iterating over.
    Create a new one and add to it."""

    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    active_users = {}
    for i in users:
        print(i)
        if users[i] == 'active':
            active_users[i] = users[i]

    print(active_users)

