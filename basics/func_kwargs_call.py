def parrot(voltage, state='state', action='action', type='type'):
    print(voltage)
    print(state)
    print(action)
    print(type)


parrot(1)


parrot(1, 's')

parrot(1, state='s')

parrot(voltage=1, state='s')

parrot(state='s', voltage=1)

'''
This returns error:
parrot() - 1 argument (voltage) required

parrot(voltage=1, 's') - non-kwarg cannot come after kwarg

parrot(1, voltage=2) - gave an argument twice

parrot(guy='me') - no such argument exists


