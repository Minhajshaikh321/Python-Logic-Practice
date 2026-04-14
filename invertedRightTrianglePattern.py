
#interview question: print the following pattern for n=5
n=5
def inverted_triangle_star_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("#",end=" ")
        for k in range(i,n):
            print("*",end=" ")      
        print()
inverted_triangle_star_pattern(n)

#Time Complexity: O(n^2)