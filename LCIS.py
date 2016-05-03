def lcis(a,b,m,n):
    M=[[0 for col in range(n)] for row in range(m)]
    for i in xrange(n):
        if b[i]==a[0]:
            for t in range(i,n):
                M[0][t]=1
            break
    for j in xrange(m):
        if a[j]==b[0]:
            for t in range(j,m):
                M[t][0]=1

    for i in range(1,m):
        for j in range(1,n):
            if a[i]==b[j]:
                M[i][j]=max(max(M[i-1][j],M[i][j-1]),M[i-1][j-1]+1)
            else:
                M[i][j]=max(M[i-1][j],M[i][j-1])
    for i in range(m):
        print M[i]
a=[3,5,6,8,9,1,2]
b=[1,2,3,6,20,8,15]
lcis(a,b,len(a),len(b))