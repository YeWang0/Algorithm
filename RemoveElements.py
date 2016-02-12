def Remove_Elements(nums,value):

    while 1:
        try:
            nums.pop(nums.index(value))
            print nums
        except:
            break
    return nums
print Remove_Elements([1,2,3,4,4,2,3,1],4)