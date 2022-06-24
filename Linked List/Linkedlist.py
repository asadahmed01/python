# A single node of a singly linked list
from hashlib import new
from locale import currency
from operator import le

from pkg_resources import parse_version


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

    def delete_node(self, data):
        # if the node being deleted is the head
        current = self.head
        # if the node is the head
        if current and current.data == data:
            self.head = current.next
            current = None
        # if the node being delete is not the head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        # if current is None, we reached the end of the list
        if current is None:
            return
        prev.next = current.next
        current = None

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printLL(self):
        current = self.head
        while current:
            print(current.data)

            current = current.next

    def swap_nodes(self, n1, n2):
        node1 = self.head
        node2 = self.head
        prevNode1 = None
        prevNode2 = None
        # check if the list is empty
        if self.head == None:
            return
        # check if n1 and n2 are the same
        if n1 == n2:
            return
        # search for node1
        while node1 is not None and node1.data != n1:
            prevNode1 = node1
            node1 = node1.next
        # search for node2
        while node2 is not None and node2.data != n2:
            prevNode2 = node2
            node2 = node2.next
        # if either node1 or node2 doesnt exist
        if not node1 or not node2:
            return
        # if node1 is not head
        if prevNode1 != None:
            prevNode1.next = node2
        # if node1 is head, make node2 the head now
        else:
            self.head = node2
        if prevNode2 != None:
            prevNode2.next = node1
        else:
            self.head = node1
        # make the swap now:
        temp = node1.next
        node1.next = node2.next
        node2.next = temp

    def swapPairs(self):
        dummy = Node(0, self.head)
        prev = dummy
        current = self.head

        while current and current.next:
            # save next pair to be swapped
            nxtPair = current.next.next
            second = current.next
            # reverse the current pair
            second.next = current
            current.next = nxtPair
            prev.next = second

            # update the ptrs
            prev = current
            current = nxtPair

        self.head = dummy.next

    def removeNode(self, val):
        dummy = self.head
        prev = self.head
        curr = self.head

        while curr:
            nxt = curr.next
            if curr.data == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        self.head = dummy

    def remove_nth_node(self, n):
        dummy = Node(0, self.head)
        left = dummy
        right = self.head

        # start moving the right ptr n nodes from the left ptr
        while n > 0 and right:
            print(n)
            right = right.next
            n -= 1
        # Now start moving both ptrs by one node

        while right:
            right = right.next
            left = left.next
        # now delete the nth node from the end

        left.next = left.next.next
        self.head = dummy.next

    def removeDuplicate(self):
        left = self.head
        right = self.head.next
        while right:
            tmp = right.next
            if left.data == right.data:
                left.next = tmp
                right = tmp
            else:
                left = left.next
                right = right.next
        return self.head

    def rotateList(self, k):
        if not self.head:
            return
        # find the length of the list
        length = 1
        tail = self.head
        curr = self.head
        while tail.next:
            tail = tail.next
            length += 1
        # aggregate the length
        k = k % length
        # get to the point where we need to do the rotation

        for i in range(length - k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        tail.next = self.head
        return newHead


# linkedlist with singl node
ll = LinkedList()  # head pointing to empty list (Null)
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(3)
# ll.insert_at_end("E")

# ll.insert_at_begining(0)
# ll.insert_at_middle(ll.head.next, "X")
# ll.delete_node("B")
ll.printLL()
print("--------------")
# ll.reverse()
# ll.swap_nodes("A", "D")
# ll.swapPairs()
# ll.removeNode("D")
# ll.remove_nth_node(2)
ll.removeDuplicate()
ll.printLL()
