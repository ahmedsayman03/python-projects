def del_inactive():
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    # print("items: ", users.copy().items())
    # above line shows key, value
    # so to loop over it:
    # for key, value in users.copy().items()
    for i in users.copy():
        print(i)
        print(users[i])
        if users[i] == 'inactive':
            users.pop(i)
    print(users)



def add_active():
    '''
    Does what the above code does, but instead creates
    new dictionary and adds active keys to it
    '''
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    active_users = {}
    for i in users:
        print(i)
        if users[i] == 'active':
            active_users[i] = users[i]

    print(active_users)

add_active()
