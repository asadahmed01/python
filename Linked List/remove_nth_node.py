# remove nth node from the end of the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_node(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # start moving the fast ptr n nodes from the slow ptr
        while fast and n <= 0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
