from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # convert the linkedlist to array
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        # check if it is palindrome
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1

        return True
