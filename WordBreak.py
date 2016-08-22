def wordbreak(s,wordDict):
    n=len(s)
    dp=[0 for i in xrange(n)]
    for i in xrange(n):
        if s[:i+1] in wordDict:
            dp[i]=1
        else:
            for j in xrange(i+1):
                if dp[j]==1:
                    if s[j+1:i+1] in wordDict:
                        dp[i]=1
                        break
    print dp

wordDict=['a','b','c','bcdf','d','e']
wordbreak('abcde',wordDict)


