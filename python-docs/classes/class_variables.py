class Dog:
    """Dogs. Have class variables (shared among all instances, a canine) and instance vars (name, unique to instance)"""
    type = 'canine'

    def __init__(self, name):
        self.name = name
        # tricks are not shared among all dogs, they are unique per dog instance
        # so it goes in the init
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Bob')
f = Dog('Joe')

print(d.name)
print(f.name)
print(d.type)
print(f.type)
d.add_trick('jump')
print(d.tricks)
print(f.tricks)
