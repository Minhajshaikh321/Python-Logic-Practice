nums=[2,7,11,15]
target=13

def target_sum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target and i!=j:
                return [i,j]
print(target_sum(nums,target))