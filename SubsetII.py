def subset2(nums):
    list=nums
    n=len(nums)
    result=[]
    def combine(n,k):
        # pick n numbers from k
        def pick(list,ln,pre):
            if ln==0 and pre not in result:
                result.append(pre)
                return
            if list==[]:
                return

            for i in xrange(len(list)):
                temp=pre[:]
                temp.append(list[i])
                pick(list[i+1:],ln-1,temp)
        def Opick(list,ln,pre):
            if ln==0 and pre not in result:
                result.append(pre)
                return
            if list==[]:
                return

            for i in xrange(len(list)):
                temp=pre[:]
                temp.remove(list[i])
                Opick(list[i+1:],ln-1,temp)

        # pick(list,k,[])

        if 2*k>n:
            k=n-k
            Opick(list,k,list)
        else:
            pick(list,k,[])


        print result
    for i in xrange(n+1):
        combine(n,i)
print subset2([1,2,2])

