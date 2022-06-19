class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        return dummy.next
