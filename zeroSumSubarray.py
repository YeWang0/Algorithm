def zeroSumSubarray(nums):
    result=[]
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum==0:
                result.append([i,j])
    print result
zeroSumSubarray([0,1,2,3,4,5,-5,-4,-3,-2,-1])