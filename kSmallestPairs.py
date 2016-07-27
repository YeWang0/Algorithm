def kSmallestPairs(nums1,nums2,k):
    a1,b2=0,0
    a2,b1=1,1
    result=set()
    result.add((0,0))
    list=[[nums1[0],nums2[0]]]
    t1=nums1[a1]+nums2[a2]
    t2=nums1[b1]+nums2[b2]
    l1=len(nums1)
    l2=len(nums2)
    while 1:
        print t1,t2
        if len(list)==k:
            return list
        if t1<=t2:
           print [a1,a2],1
           if (a1,a2) not in result:
               result.add((a1,a2))
               list.append([nums1[a1],nums2[a2]])
           # a2+=1
           while (a1,a2) in result:
               a2+=1
               if a2>=l2:
                   a1+=1
                   a2=0
                   if a1>=l1:
                       break
               # if a1==b1 and a2==b2:
               #     a2+=1
           if a1>=l1:
               break
           t1=nums1[a1]+nums2[a2]
        else:
            print [b1,b2],2
            if (b1,b2) not in result:
                result.add((b1,b2))
                list.append([nums1[b1],nums2[b2]])
            # b1+=1
            while (b1,b2) in result:
                b1+=1
                if b1>=l1:
                    b2+=1
                    b1=0
                    if b2>=l2:
                        break
                # if a1==b1 and a2==b2:
                #    b1+=1
            if b2>=l2:
                break
            t2=nums1[b1]+nums2[b2]
    # print result
    return list
# [-10,-4,0,0,6]
# [3,5,6,7,8,100]
nums1=[-10,-4,0,0,6]
nums2=[3,5,6,7,8,100]
k=10
print kSmallestPairs(nums1,nums2,k)
