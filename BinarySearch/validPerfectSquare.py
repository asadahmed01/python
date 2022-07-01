def isPerfectSquare(num) -> bool:
    # Brute force soluton (loop)
    # for i in range(1, num + 1):
    #     if i * i == num:
    #         return True
    #     if i * i > num:
    #         return False

    # optimized solution (binary search)
    start = 1
    end = num
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == num:
            return True
        if mid * mid < num:
            start = mid + 1
        if mid * mid > num:
            end = mid - 1
    return False


print(isPerfectSquare(3))
