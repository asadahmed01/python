# Desing a circular queue
class ListNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class MycircularQueue:
    def __init__(self, k):
        # k is the number of spaces in the queue
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value, self.right, self.left)
        self.right.prev.next = node
        self.right.prev = node
        self.space - +1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        # the queue is empty if the left node is pointing to the right node
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0

    def display(self):
        if self.isEmpty():
            print("Empty")
        curr = self.left.next
        while curr != self.right:
            print(curr.val)
            curr = curr.next


cq = MycircularQueue(4)
cq.enQueue(1)
cq.enQueue(2)
cq.enQueue(3)
cq.enQueue(4)
cq.deQueue()
cq.deQueue()
cq.deQueue()
cq.deQueue()
cq.display()
