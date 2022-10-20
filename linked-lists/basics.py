class LinkedListFirst:
    """A linked list is a sequence of DS connected with a link.

    Link: Stores data, and has
        next: link to next link

    LL = connection link to first link "First"

    i.e. Chain of nodes, each node points to next node

    Link FIRST (all LL have this)

    Link (data, next - next link)

    Last (last link, next = None)

    TYPES:
    Simple
        goes right

    Doubly
        Has previous and next

    Circular
        First node connects to last with prev and last node connects to first with next

    OPS
    insert at beginning

    delete beginning

    display - show list

    search - using key (element)

    delete - using given key / elem"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def insert(self, node):
        """Insert node at start of a list."""
        # Create new (not head) node that has same data as self
        link_node = Node(self.data, self.next_node)

        # Unlink self from sequence
        self.next_node = None

        # Link new head node to previous head node
        node.next_node = link_node

    def __str__(self):
        l = []
        curr_node = self
        while curr_node:
            l.append(curr_node.data)
            curr_node = curr_node.next_node

        return str(l)

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.next_node


class Node:
    """A node in a linked list contains data and a next link to another node."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


a = Node(1, None)
b = Node(2, a)
c = Node(3, b)
d = Node(4, c)
f = LinkedListFirst(0, d)
print(f)
h = LinkedListFirst(999)
f.insert(h)
print(h)

for i in h:
    print(i.data)
