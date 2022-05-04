from operator import indexOf

# brute force solution
def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([nums[i], nums[j]])


nums = [2, 7, 11, 15]

# optimized solution
def towSum_optimized(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        print(complement)
        if complement in seen:
            print(seen)
            return [nums[complement], i]
        else:
            seen[nums[i]] = n


# nums = [3, 2, 4]
target = 9
two_sum(nums, target)
print(towSum_optimized(nums, 9))
