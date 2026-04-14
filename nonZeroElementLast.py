#Interview Question: Given an array of integers, move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements.
def non_zero_element(arr):
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos],arr[i]=arr[i],arr[pos]
            pos+=1
    return arr
print(non_zero_element([0,1,0,3,12]))  # [1,3,12,0,0]

#Time complexity: O(n) where n is the length of the array. We traverse the array once to move the non-zero elements and then fill the remaining positions with zeroes.
#Space complexity: O(1) since we are modifying the array in place and not using any additional data structures that grow with the input size.