def merge_sort(first_list, second_list):
    result = []
    i = j = 0

    while i < len(first_list) and j < len(second_list):
        if first_list[i] < second_list[j]:
            result.append(first_list[i])
            i += 1
        else:
            result.append(second_list[j])
            j += 1

    if i < len(first_list):
        result.extend(first_list[i:])
    else:
        result.extend(second_list[j:])

    return result


def separate_list(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = separate_list(array[:mid])
    right = separate_list(array[mid:])

    return merge_sort(left, right)
