def bubble_sort(arr, reverse=False):
    arr=arr[:]
    n=len(arr)
    print(n)
    for i in range(n):
        for j in range(0,n-i-1):
            if reverse:
                cond=arr[j]<arr[j+1]
            else:
                cond=arr[j]>arr[j+1]
            if cond:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
nums = [5, 2, 8, 1, 9, 3]
bubble_sort(nums,True)
