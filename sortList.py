#Interview Question: Given a list of integers, sort the list in ascending order using the insertion sort algorithm.
def sort_lst(lst):
    for i in range(len(lst)):
        while i>0 and lst[i]>lst[i-1]:
            lst[i],lst[i-1]=lst[i-1],lst[i]
            i-=1    
    return lst

lst=[30,81,15,5]
sort_lst(lst)

#Time complexity: O(n^2) in the worst case when the list is sorted in reverse order. In the best case when the list is already sorted, the time complexity is O(n).