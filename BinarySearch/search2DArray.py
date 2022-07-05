def search2D(matrix: list[list[int]], target) -> bool:
    # if matrix is empty
    if not matrix or not matrix[0]:
        return False
    # now look for the row in which our target lies
    row = 0

    for r in range(len(matrix)):
        if target == matrix[r][0] or target == matrix[r][-1]:
            return True
        elif target > matrix[r][0] and target < matrix[r][-1]:
            row = r
            break
    # now do binary search on that row
    l = 0
    r = len(matrix[row]) - 1
    while l <= r:
        m = (l + r) // 2
        if m < target:
            l = m + 1
        elif m > target:
            r = m - 1
        else:
            return True


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(search2D(matrix, 33))
