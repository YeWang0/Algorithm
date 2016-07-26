
Count=0
# brutal
def combinationSum(nums,target):
    global Count
    for i in xrange(len(nums)):
        x=target-nums[i]
        if x>0:
            combinationSum(nums,x)
        elif x==0:
            Count+=1

nums = [1,2,3]
target = 4

# combinationSum(nums,target)

print Count


# dp
def combinationSum4(nums,target):
    # init
    if not nums:
        return 0
    if min(nums)>target:
        return 0
    dp=[1]+[0]*target
    for i in xrange(target+1):
        if dp[i]!=0:
            for j in nums:
                if i+j<=target:
                    dp[i+j]+=dp[i]
    return dp[target]

combinationSum4(nums,target)