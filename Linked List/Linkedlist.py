# A single node of a singly linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# create a single node
# first = Node(1)
# print(f"{first.data}--> {first.next}")
# A linked list class with a single heade node (empty)


class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# linkedlist with singl node
ll = LinkedList()  # head pointing to empty list (Null)
ll.insert(0)
ll.insert(1)
ll.insert(2)
ll.printLL()
