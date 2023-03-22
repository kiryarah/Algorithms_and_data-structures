def binary_search(array, search_num):
    mid = len(array) // 2
    left, right = 0, len(array) - 1

    while left < right and array[mid] != search_num:
        if search_num > array[mid]:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2

    if array[mid] > search_num:
        mid += 1

    return mid + 1 if mid < len(array) else 0
