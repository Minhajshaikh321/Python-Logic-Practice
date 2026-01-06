arr = [2,1,4,3,1,4,2,5]
def unique_num(arr):
    return [i for i in arr if arr.count(i)<2]
print(unique_num(arr))