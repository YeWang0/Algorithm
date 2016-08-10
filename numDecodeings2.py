def numDecodings(s):
    def belong(x):
        if x<3:
            return x
        else:
            return 3

    if not s:
        return 0
    n=len(s)

    if s[0]=='0':
            return 0
    for i in xrange(1,n):
        if s[i]=='0' and s[i-1]!='1' and s[i-1]!='2':
            return 0

    DP=[[0 for i in xrange(4)]for j in xrange(n)]
    # print DP
    DP[0][belong(int(s[0]))]=1



    def update(pre,x):
        type=belong(x)
        result=[0,0,0,0]
        if type==0:
            result[3]=pre[1]+pre[2]
        elif type==1:
            result[1]=pre[1]+pre[2]+pre[3]
            result[3]=pre[1]+pre[2]
        elif type==2:
            result[2]=pre[1]+pre[2]+pre[3]
            result[3]=pre[1]+pre[2]
        else:
            if x<7:
                result[3]=(pre[1]+pre[2])*2+pre[3]
            else:
                result[3]=pre[1]*2+pre[2]+pre[3]
        return result
    for i in xrange(1,n):
        DP[i]=update(DP[i-1],int(s[i]))
    return sum(DP[-1])



numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")