def setZeros(matrix):
    m=len(matrix)
    n=len(matrix[0])
    x=[0 for i in xrange(m)]
    y=[0 for i in xrange(n)]
    tp=[0 for i in xrange(n)]
    for i in xrange(m):
        for j in xrange(n):
            if not x[i] or not y[j]:
                if not matrix[i][j]:
                    if not x[i]:
                        x[i]=1
                    if not y[j]:
                        y[j]=1
    for i in xrange(m):
        if x[i]:
            matrix[i]=tp
    for j in xrange(n):
        if y[j]:
            for i in xrange(m):
                matrix[i][j]=0

matrix=[[1,2,3,4,5],[1,2,3,4,5],[1,2,0,4,5]]
setZeros(matrix)
print matrix
