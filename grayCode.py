def grayCode(n):
    def switch(list):
        # print list
        result=[]
        for i in xrange(len(list)-1,-1,-1):
            temp=list[:]
            temp[i]=1-temp[i]
            # print temp
            result.append(temp)
        return result
    def trans(list):
        x=0
        for i in list:
           x=x*2+i
        return x
    base=[[0 for i in xrange(n)]]
    final=[0]
    p=0
    e=1
    while p<e:

        result=switch(base[p])
        # print result
        for i in result:
            if i not in base:
                base.append(i)
                final.append(trans(i))
                e+=1
                break
        p+=1
    print final

grayCode(2)


