def removeDuplication(nums):
    i=0
    n=len(nums)-1
    while i<n:
        if nums[i]==nums[i+1]:
            nums=nums[:i]+nums[i+1:]
            n-=1
        else:
            i+=1
    return nums

def wiggle(nums):
    nums=removeDuplication(nums)
    wig=[0]*(len(nums)-1)
    for i in xrange(len(nums)-1):
        wig[i]=(nums[i+1]-nums[i])>0
    # print wig
    wig=removeDuplication(wig)
    return len(wig)+1

nums=[1,7,4,9,2,5]
wiggle(nums)