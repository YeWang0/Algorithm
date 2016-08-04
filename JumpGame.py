def jumpGame(nums):
    global count
    count=0
    def jump(jumped,position):
        global count
        if position+nums[position]>=len(nums)-1:
            count+=1
        for i in xrange(max(position-nums[position],0),min(position+nums[position],len(nums)-1)+1):
            if i not in jumped:
                temp=jumped[:]
                temp.append(i)
                jump(temp,i)
    jump([],0)
    return count
nums=[1,2,2,6,3,6,1,8,9,4,7,6,5,6,8,2,6,1,3,6,6,6,3,2,4,9,4,5,9,8,2,2,1,6,1,6,2,2,6,1,8,6,8,3,2,8,5,8,0,1,4,8,7,9,0,3,9,4,8,0,2,2,5,5,8,6,3,1,0,2,4,9,8,4,4,2,3,2,2,5,5,9,3,2,8,5,8,9,1,6,2,5,9,9,3,9,7,6,0,7,8,7,8,8,3,5,0]

# print jumpGame(nums)

def jumpGameII(nums):
    reach=0
    dest=len(nums)-1
    i=0
    while i < (min(reach,dest)+1):
        reach=max(i+nums[i],reach)
        i+=1
    return reach>=dest
print jumpGameII(nums)