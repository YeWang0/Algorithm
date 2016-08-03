def rotateSquare(Matrix):
    n=len(Matrix)
    # result=[[0 for j in xrange(n)]for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(i+1,n):
            Matrix[i][j],Matrix[j][i]=Matrix[j][i],Matrix[i][j]
    for i in xrange(n//2):
        for j in xrange(n):
            Matrix[j][i],Matrix[j][n-1-i]=Matrix[j][n-1-i],Matrix[j][i]
Matrix=[[1,2,3],[4,5,6],[7,8,9]]
rotateSquare(Matrix)
rotateSquare(Matrix)
rotateSquare(Matrix)
rotateSquare(Matrix)
print Matrix
