
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # if num
    store=[]
    result=len(nums)
    n=len(nums)
    i=0
    while i<n:
        if not store:
            store.append(nums[i])
            i+=1
        elif nums[i] not in store:
            store=[nums[i]]
            i+=1
        elif len(store)==1:
            store.append(nums[i])
            i+=1
        else:
            nums.remove(nums[i])
            n-=1

    # nums=list[:]
    # print nums
    return n

nums=[1,1,1,2,2,2,3,3,3]
removeDuplicates(nums)