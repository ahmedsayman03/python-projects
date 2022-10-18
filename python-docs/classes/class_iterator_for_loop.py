class Schools:
    """Class with a for loop that goes backwards"""
    def __init__(self, primary_schools):
        self.primary_schools = primary_schools
        self.index = len(primary_schools)

    def __iter__(self):
        """Defines for loop. Returns next item. if __next__ defined, return self."""
        return self

    def __next__(self):
        """Return next item. If 0, raise StopIteration."""
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        # Note: this is a backwards loop
        return self.primary_schools[self.index]


s = Schools('spam')

for i in s:
    print(i)


"""The way for loop works is it calls iter() in obj
iter returns obj that has next() that goes to next item
no more items? It raises StopIteration exception that tells for loop to terminate
you can call next():"""
s = 'abc'
it = iter(s)
print(next(it))
print(next(it))
print(next(it))


def re(data):
    """Generators are like class based iterators but iter and next are created automatically.

    yield something when they want to return it. when next() is called, it continues where it left off,
    local vars and execution state is remembered.

    raise StopIteration when terminating.

    So you can use this in for loops."""
    for char in range(len(data)-1, -1, -1):
        yield data[char]


for i in re('testing'):
    print(i)


def generator_expression():
    """Like list comprehensions, we have generator comprehensions."""
    g = (i*i for i in range(10))
    print(g)  # generator
    # Basically, g will yield for i, then another i, then another i, whenever next is called

    # Useful if it's enclosed with a function
    print(sum(g))

    # valedictorian = max(((student.gpa, student.name) for student in graduates))
    # Above is a generator that keeps giving (gpa, name) tuple seperated by comas (you can think of it like this)
    # so the max function can use it.


generator_expression()
