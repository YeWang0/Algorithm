def spiral(Matrix):
    x=0
    y=0
    n=len(Matrix)
    m=len(Matrix[0])
    max=m*n
    count=0
    while (count<=max):
        if x*2+1==n and y*2+1==m:
            print Matrix[x][y]
        else:
            for i in xrange(y,m-y-1):
                print Matrix[x][i]
                count+=1
                if count==max:
                    break
            for i in xrange(x,n-x-1):
                print Matrix[i][m-y-1]
                count+=1
                if count==max:
                    break
            for i in xrange(m-y-1,y,-1):
                print Matrix[n-x-1][i]
                count+=1
                if count==max:
                    break
            for i in xrange(n-x-1,x,-1):
                print Matrix[i][y]
                count+=1
                if count==max:
                    break
            x+=1
            y+=1
Matrix=[[1,2],[6,3],[5,4]]

spiral(Matrix)
# spiral(Matrix,1,1)