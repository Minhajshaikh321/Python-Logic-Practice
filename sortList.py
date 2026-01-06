#sort the list in ascending order
def sort_lst(lst):
    for i in range(len(lst)):
        while i>0 and lst[i]<lst[i-1]:
            lst[i],lst[i-1]=lst[i-1],lst[i]
            i-=1    
    return lst

lst=[81,32,15,5,26]
sort_lst(lst)