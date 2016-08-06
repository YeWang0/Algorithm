def combine(n,k):
    # pick n numbers from k
    list=[i for i in xrange(1,n+1)]
    result=[]
    def pick(list,ln,pre):
        if ln==0:
            result.append(pre)
            return
        if list==[]:
            return

        for i in xrange(len(list)):
            temp=pre[:]
            temp.append(list[i])
            pick(list[i+1:],ln-1,temp)
    def Opick(list,ln,pre):
        if ln==0:
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
combine(20,16)
