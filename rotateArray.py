#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]
def rotate_array(lst,k):
    
    for i in range(k):
        n=lst.pop()
        lst.insert(0,n)
    return lst

lst=[1,2,3,4,5,6,7]
print(rotate_array(lst,3))