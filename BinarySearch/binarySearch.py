def binarySearch(nums, target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        # print(mid)
        if target == nums[mid]:
            return mid
        # if target is less than mid
        if target < mid:
            end = mid - 1

        # if target is greater than mid
        if target > mid:
            start = mid + 1

    return -1


nums = [1, 2, 3, 4, 5, 6]
target = 9
print(binarySearch(nums, target))
