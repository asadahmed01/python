from operator import indexOf


def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([nums[i], nums[j]])


# nums = [2, 7, 11, 15]
nums = [3, 2, 4]
target = 6
two_sum(nums, target)
