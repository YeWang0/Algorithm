def trapWater(boundary):
    top=0
    total=0
    cur=0

    for idx,i in enumerate(boundary):
        # print total
        if i>=top:
            top=i
            index=idx
            if cur!=0:
                total+=cur
                cur=0
        else:
            cur+=top-i
    if cur:
        top=0
        cur=0
        for idx,i in enumerate(boundary[idx::-1]):
            # print total
            if i>=top:
                top=i
                index=idx
                if cur!=0:
                    total+=cur
                    cur=0
            else:
                cur+=top-i
    return total

boundary=[0,1,0,2,1,0,1,3,2,1,2,1]

print trapWater(boundary)
