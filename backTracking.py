# leetcode 46 Permutations
def permute(nums):
    n=len(nums)
    ans,sol=[],[]
    def backtrack():
        if len(sol)==n:
            ans.append(sol[:])
            return 
        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()
    backtrack()
    return ans
print(permute([1,2,3]))


# def permute(nums):
#     res=[]
#     def backtrack(idx):
#         if idx==len(nums):
#             res.append(nums[:])
#             return
#         for i in range(idx,len(nums)):
#             nums[idx],nums[i]=nums[i],nums[idx]
#             backtrack(idx+1)
#             nums[idx],nums[i]=nums[i],nums[idx]
#     backtrack(0)
#     return res
# print(permute([1,2,3]))
