def minTotal(triangle):
    n=len(triangle)
    DP=[[float('Inf') for x in xrange(i)] for i in xrange(1,n+1)]
    DP[0]=triangle[0]
    print DP
    def getMin(row,colum):

        if colum==0 or colum==row:
            return DP[row-1][max(colum-1,0)]
        else:
            return min(DP[row-1][colum],DP[row-1][colum-1])
    for i in xrange(1,n):
        for j in xrange(i+1):
            # print [i,j]
            # print getMin(i,j)
            DP[i][j]=getMin(i,j)+triangle[i][j]
    print DP


triangle=[[1],[2,3],[4,5,6]]
minTotal(triangle)