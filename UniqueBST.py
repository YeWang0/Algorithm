def uniqueBST(n):
    dp=[0 for i in xrange(n)]
    dp[1]=1
    for i in xrange(2,n):
        dp[i]=dp[i-1]*2+dp[i-2]
    print dp
    return dp[-1]

uniqueBST(10)
