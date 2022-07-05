def findMin(nums: list[int]) -> int:
    res = nums[0]
    l = 0
    r = len(nums) - 1
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        # do binary search
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            # search the right side
            l = m + 1
        else:
            r = m - 1
        return res
