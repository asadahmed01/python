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
    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            # traverse to the last node
            while current.next:
                current = current.next
            # when you find the last node, point it to the new node
            current.next = node

    def insert_at_begining(self, data):
        # create new node
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_middle(self, prev_node, data):
        if not prev_node:
            print(f"{prev_node} is not in the list")
            return
        # create the new node
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def printLL(self):
        current = self.head
        while current:
            print(current.data)

            current = current.next


# linkedlist with singl node
ll = LinkedList()  # head pointing to empty list (Null)
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_begining(0)
ll.insert_at_middle(ll.head.next.next, 7)
ll.printLL()
