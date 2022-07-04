from unicodedata import mirrored


def guessNumber(n: int) -> int:
    left = 0
    right = n

    while True:
        mid = left + right // 2
        res = guess(mid)
        if res > 0:
            left = mid + 1
        if res < 0:
            right = mid - 1
        else:
            return mid
