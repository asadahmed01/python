# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left(nums):
    return nums[1:] + nums[:1]


# print(rotate_left([1, 2, 3]))

# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


def count_evens(nums):
    count = 0
    for i, n in enumerate(nums):
        if n % 2 == 0:
            count += 1
    return count


# print(count_evens([2, 1, 2, 3, 4]))

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            break
        sum += nums[i]
    return sum


print(sum13([1, 2, 2, 1, 13]))
