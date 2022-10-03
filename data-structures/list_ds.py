'''
List

list.append(x)


list.extend(iterable)
append items to end of list

list.insert(i, x)
insert x at i

list.remove(x)
remove x. no x: error

list.pop([i])
remove last item, or item at position i. Note: [] denotes optional

list.clear()
del a[:]

del a[4] and l.pop(4) differ in that pop returns a value

list.index(x[, start[, end]])
returns index of x. optional: index of x in sliced list

list.count(x)
number of times x in list

list.sort(key=None, reverse=False)
sort based on function key. reverse if you want

list.reverse()

list.copy()
a[:]

List as stack (LIFO)
l.append()
l.pop()

List as queue (FIFO)
l.insert(0, x)
l.pop(0)

This is slow! because all elements have to be shifted.
collections.deque has fast appends and pops from both ends.

'''
