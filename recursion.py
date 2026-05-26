# def recusrionNum(n):
#   if n==0:
#     return 
# #   print(n)
#   recusrionNum(n-1)
#   print(n)
# recusrionNum(3)
lst=[1,2,3,4,5]
# print(len(lst))
for i in range(1,len(lst),2):
    # print(i)
    lst[i],lst[i-1]=lst[i-1],lst[i]
    print(lst)