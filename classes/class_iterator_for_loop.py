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
iter(s)

for char in s:
    print(char)


"""The way for loop works is it calls iter() in obj
iter returns obj that has next() that goes to next item
no more items? It raises StopIteration exception that tells for loop to terminate
you can call next():"""
s = 'abc'
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
