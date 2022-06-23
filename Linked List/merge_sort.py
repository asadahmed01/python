def mergeSort(arr):

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)

    # return the merged arrays
    return merge_arrays(leftArr, rightArr)


def merge_arrays(left, right):
    sorted_arr = []
    j = 0
    k = 0
    while j < len(left) and k < len(right):
        if left[j] <= right[k]:
            sorted_arr.append(left[j])
            j += 1
        else:
            sorted_arr.append(right[k])
            k += 1
    while j < len(left):
        sorted_arr.append(left[j])
        j += 1
    while k < len(right):
        sorted_arr.append(right[k])
        k += 1
    return sorted_arr


arr = [5, 1, 8, 6, 7, 2, 3]
print(mergeSort(arr))
