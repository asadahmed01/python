class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(fast)
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


nums = [1, 3, 4, 2, 2]
s = Solution()
s.findDuplicate(nums)
