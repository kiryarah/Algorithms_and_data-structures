def binary_search(array, search_num):
    mid = len(array) // 2
    left, right = 0, len(array) - 1

    while left <= right:
        if array[mid] == search_num:
            return mid
        
        if search_num > array[mid]:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2

    return -1
