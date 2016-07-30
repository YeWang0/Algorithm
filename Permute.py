result=[]
def permute(nums,list):
    if len(nums)==0 :
        # and list not in result:
        result.append(list)
    else:
        s=set()
        for i in xrange(len(nums)):
            if nums[i] not in s:
                temp=list[:]
                temp.append(nums[i])
                permute(nums[:i]+nums[i+1:],temp)
                s.add(nums[i])
permute([1,1,2],[])
print result