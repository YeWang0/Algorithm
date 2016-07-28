def multipleStrings(a,b):
    def multiple(ax,x):
        if x==0:
            return []
        result=[]
        carry=0
        for i in ax[::-1]:
            t=i*x
            if carry>0:
                t+=carry
            if t>9:
                carry=t//10
                result.append(t%10)
            else:
                carry=0
                result.append(t)
        if carry!=0:
            result.append(carry)
        return result
    def add(mx,nx):
        m=mx[:]
        n=nx[:]
        # print m,n
        # print '---'
        if m==[]:
            return n
        if n==[]:
            return m
        result=[]
        if len(m)>len(n):
            m,n=n,m
        carry=0
        for i in xrange(len(m)):
            t=m[i]+n[i]
            if carry==1:
                t+=1
            if t>9:
                carry=1
                result.append(t%10)
            else:
                carry=0
                result.append(t)
        if len(n)>len(m):
            if carry==1:
                temp=add([1],n[len(m):])
                result.extend(temp)
            else:
                result.extend(n[len(m):])
        else:
            if carry==1:
                result.append(1)
        return result
    def updateSet(dict):
        for i in dict.keys():
            dict[i].insert(0,0)

    ax=[]
    bx=[]
    for i in a:
        ax.append(int(i))
    for i in b:
        bx.append(int(i))
    an=set(ax)
    bn=set(bx)
    if len(an)<len(bn):
        ax,bx=bx,ax
        an,bn=bn,an
    dict={}
    for i in bn:
        dict[i]=multiple(ax,i)
    print dict
    result=[]
    for i in bx[::-1]:
        result=add(result,dict[i])
        # print  result
        # print '~~'
        updateSet(dict)
    if result==[]:
        return 0
    return result[::-1]




print multipleStrings('98','9')