def bubble_sort(arr: list[int]) -> list[int]:
    result = arr.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


result = bubble_sort([3, 2, 1, 12, 51, -1])
print(result)   