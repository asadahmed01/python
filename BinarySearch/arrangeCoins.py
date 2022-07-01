def arrangeCoins(num) -> int:
    rows = 0
    for i in range(1, num + 1):
        num = num - i
        # print(remaing)
        if num < i:
            break
        rows += 1
    return rows


print(arrangeCoins(5))
