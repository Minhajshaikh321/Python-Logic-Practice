#Interview Question: Given a list of numbers, find the largest number in the list.
lt=[32,15,81,5,26]
num=0
for i in lt:
    if i>num:
        num=i
print("The largest number in the list is:",num)

#Time complexity: O(n) where n is the length of the list. We need to iterate through the entire list once to find the largest number.
#Space complexity: O(1) since we are using only a constant amount of extra space to store the largest number.