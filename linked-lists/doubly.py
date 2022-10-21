class Node:
    """A node for a doubly linked list, containing data, previous and next link to node."""
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """A linked List where each link contains a previous and next link."""
    def __init__(self):
        self.head = None

    def insert(self, node):
        """Inserts node into the start of the list."""
        node.next = self.head
        if self.head:
            self.head.prev = node

        self.head = node
        node.prev = None

    def delete(self):
        """Deletes node at the beginning of the list."""
        old_head = self.head
        new_head = self.head.next
        self.head = new_head
        new_head.prev = None
        old_head.next = None

    def insert_last(self, node):
        """Adds node to the last part of the list."""
        current = self.head
        while current.next:
            current = current.next

        else:
            current.next = node
            node.prev = current
            node.next = None

    def delete_last(self):
        """Deletes last node in the linked list."""
        current = self.head
        while current.next is not None:
            current = current.next
        # Current node has no next, therefore it is the last note
        # Unlink current from previous node
        current.prev.next = None
        current.prev = None

    def insert_after(self, node, index):
        """Inserts node after a given index."""
        ind = 0
        current = self.head
        # Traverse list until given index is reached
        while ind is not index:
            current = current.next
            ind = ind + 1

        # Want to insert after current node
        # Want to update the next node's prev attribute to point to new node now too
        n = current.next
        current.next = node
        node.prev = current
        node.next = n
        n.prev = node

    def delete_index(self, index):
        """Deletes node at a given index."""
        ind = 0
        current = self.head

        while ind is not index:
            current = current.next
            ind = ind + 1

        # Want to delete current node
        # Update nodes before and after current to point to each other
        current.prev.next = current.next
        current.next.prev = current.prev

        # Unlink current
        current.next = None
        current.prev = None

    def display(self):
        """Prints linked list using the data of each element."""
        print('Head', end='->')
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('\n')


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
ll = DoublyLinkedList()

ll.insert(a)
ll.insert(b)
ll.insert(c)
ll.insert(d)
ll.display()

last = Node(999)
ll.insert_last(last)

ll.display()

n = Node(50)
ll.insert_after(n, 1)
ll.display()
ll.delete_index(2)
ll.display()
