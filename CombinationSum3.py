def combinationSum3(k,n):
    s=[0,1,2,3,4,5,6,7,8,9]
    Matrix = [[[] for x in range(n+1)] for y in range(k+1)]

    for j in xrange(1,min(10,n+1)):
            if j==s[j]:
                Matrix[1][j].append([s[j]])
    # print Matrix[1]
    for i in xrange(2,k+1):
        for j in xrange(1,n+1):
            # j is sub sum
            # i is number of integer
            p=i-1
            for x in s[1:]:
                if j-x>0:
                    if len(Matrix[p][j-x])>0:
                        for sub in Matrix[p][j-x]:
                            temp=sub[:]
                            if x not in temp:
                                temp.append(x)
                                temp.sort()
                                if temp not in Matrix[i][j]:
                                    Matrix[i][j].append(temp)
    for i in Matrix:
        print i
        print '-'
    return Matrix[k][n]



print combinationSum3(3,21)

# print set(x)

