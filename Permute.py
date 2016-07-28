result=[]
def permute(nums,list):
    if len(nums)==0:
        result.append(list)
    else:
        for i in xrange(len(nums)):
            temp=list[:]
            temp.append(nums[i])
            permute(nums[:i]+nums[i+1:],temp)
permute([1,2,3,4,5],[])
print result