m=10
n=8

def uniquePaths(m,n):
    x=init(m,n)
    a=1
    b=1
    while a<m and b<n:
        for i in xrange(a,n):
            x=findpath(x,i,b)
        for j in xrange(b,m):
            x=findpath(x,a,j)
        a+=1
        b+=1
    print x[n-1][m-1]

def findpath(x,a,b):
    x[a][b]=x[a-1][b]+x[a][b-1]
    return x

def init(m,n):
    x=[[]for i in xrange(n)]
    a=1
    for i in xrange(n):
        for j in xrange(m):
            x[i].append(0)

    for i in xrange(1,m):
        x[0][i]=1
    for i in xrange(1,n):
        x[i][0]=1
    return x
uniquePaths(m,n)

