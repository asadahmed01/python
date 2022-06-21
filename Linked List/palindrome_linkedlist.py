from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     # convert the linkedlist to array
    #     nums = []

    #     while head:
    #         nums.append(head.val)
    #         head = head.next

    #     # check if it is palindrome
    #     l = 0
    #     r = len(nums) - 1
    #     while l <= r:
    #         if nums[l] != nums[r]:
    #             return False
    #         l += 1
    #         r -= 1

    #     return True
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        # find the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half of the list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check for palindrome
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next

        return True
