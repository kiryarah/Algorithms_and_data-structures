'''
    Дана последовательность уникальных чисел от 1 до N.
    В последовательности удалено 2 числа. Найти их.
'''



def find_missing_numbers(arr):
    n = len(arr)
    arr.extend([1, 1])

    for i in range(n + 2):
        arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    k = 1
    for i in range(n + 2):
        if arr[i] > 0:
            print(i + 1, end=' ')
        else:
            arr[i] = -arr[i]


arr = [1, 2, 3, 4, 5, 6, 8, 9] # [4, 7]
find_missing_numbers(arr)


arr = [1, 2, 3, 4, 5, 6, 8, 9]
missing = find_missing_numbers(arr)
print(missing)  # [4, 7]
