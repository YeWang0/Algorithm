def combinationSum(candidates,target):
    if target<min(candidates):
            return []
    if not candidates:
        return []

    dp=[[] for i in xrange(target+1)]
    for i in candidates:
        if i <=target and dp[i]==[]:
            dp[i].append([i])
    print dp
    for i in xrange(min(candidates)+1,target+1):
        for j in candidates:
            if i-j>0:
                t=i-j
                if len(dp[t])>0:
                    for sol in dp[t]:
                        temp=sol[:]
                        if j not in temp or temp.count(j)+1<=candidates.count(j):
                            temp.append(j)
                            temp.sort()
                            if temp not in dp[i]:
                                dp[i].append(temp)
    for i in dp:
        print i
    return dp[target]



combinationSum([10,1,2,7,6,1,5],8)