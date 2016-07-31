def coinChange(coins,amount):
    coins.sort()
    if amount in coins:
        return 1
    elif amount<min(coins):
        return -1
    elif amount==0:
        return 0
    dp=[[] for i in xrange(amount+1)]
    for i in coins:
        if i<amount:
            dp[i].append(i)
    for i in xrange(1,amount+1):
            for j in coins:
                for x in xrange(1,amount//j+1):
                    if i-x*j>0 and dp[i-x*j]!=[]:
                        if dp[i]!=[] and len(dp[i-x*j])+x<len(dp[i]) or dp[i]==[]:
                            temp=dp[i-x*j][:]
                            # print temp
                            for t in xrange(x):
                                temp.append(j)

                            dp[i]=temp
    for i in dp:
        print i
        print ''
    return len(dp[amount])

print coinChange([205,21,66,115,396,469,202,442,364],5563)