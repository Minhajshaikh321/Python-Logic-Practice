#Leetcode Question: 1. Two Sum
#Input: nums = [2,7,11,15], target = 9
nums=[2,7,11,15]
target=18
check={}
def target_sum(nums,target):
    for i,value in enumerate(nums):
        diff=target-value
        if diff in check:
            print(check[diff],i)
        check[value]=i
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i]+nums[j]==target and i!=j:
#                 return [i,j]
print(target_sum(nums,target))