# Interview question: Given two sorted arrays, merge them in such a way that the result is also sorted.
# arr1=[1,3,4,5] arr2=[2,4,6,8,9,9]
# output=[1,2,3,4,4,5,6,8,9,9]
def merge_sort(arr1,arr2):
    i=j=0
    result=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
arr1=[1,3,4,5]
arr2=[2,4,6,8,9,9]
print(merge_sort(arr1,arr2))

#Time complexity: O(n+m) where n and m are the lengths of the two input arrays. We need to iterate through both arrays once to merge them.
#Space complexity: O(n+m) since we are creating a new array to store the merged result, which in the worst case can be as large as the sum of the lengths of the two input arrays.