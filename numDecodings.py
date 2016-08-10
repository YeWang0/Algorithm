def numDecodings(s):
    # DP
    if not s:
        return 0
    n=len(s)

    if s[0]=='0':
            return 0
    for i in xrange(1,n):
        if s[i]=='0' and s[i-1]!='1' and s[i-1]!='2':
            return 0

    DP=[[]for i in xrange(n)]
    DP[0].append([int(s[0])])
    def update(list,x):
        result=[]
        x=int(x)
        for l in list:
            if x!=0:
                temp=l[:]
                temp.append(x)
                result.append(temp)
            if l[-1]<3 and l[-1]>0:
                tp=l[-1]*10+x
                if tp<27:
                    temp=l[:]
                    temp[-1]=tp
                    result.append(temp)
        return result

    for i in xrange(n-1):
        DP[i+1]=update(DP[i],s[i+1])
    return DP[-1]
# print update([[1]],'6')
s='10'
numDecodings(s)
