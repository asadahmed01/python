class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # split the list
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        # keep splitting the list until single nodes
        left = self.sortList(self, left)
        right = self.sortList(self, right)
        return self.merge(left, right)

    def getMid(self, head):
        slow = head
        fast = head.next
        while head and head.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
