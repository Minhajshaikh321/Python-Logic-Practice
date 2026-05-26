def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print(pivot)
    left  = list(filter(lambda x: x < pivot, arr))
    mid   = list(filter(lambda x: x == pivot, arr))
    right = list(filter(lambda x: x > pivot, arr))
    return quicksort(left) + mid + quicksort(right)

nums = [26,25,24,27]
print(quicksort(nums))  # [1, 2, 3, 5, 8, 9]