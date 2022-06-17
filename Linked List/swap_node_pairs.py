class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        current = head

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

        return dummy.next
