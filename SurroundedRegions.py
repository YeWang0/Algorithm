def surround(matrix):
    n=len(matrix)
    m=len(matrix[0])

    global result
    wait=[]
    pre=circle(matrix,m,n,0,0)
    result=pre[:]
    i=1
    j=1
    while j<(n+1)//2 and i<(m+1)//2:
        # print m,n,i,j
        wait=circle(matrix,m,n,i,j)
        print wait
        group=[]
        # for p in wait:
        #     flag=False
        #     # print p,group
        #     if not group:
        #         group.append([p])
        #     else:
        #         for g in group:
        #             if adjent(p,g):
        #                 g.append(p)
        #                 flag=True
        #                 break
        #         if not flag:
        #             group.append([p])
        if wait:
            while wait:
                group.append([wait.pop()])
                for g in group:
                    for p in g:
                        if [p[0]+1,p[1]] in wait:
                            wait.remove([p[0]+1,p[1]])
                            g.append([p[0]+1,p[1]])
                        if [p[0]-1,p[1]] in wait:
                            wait.remove([p[0]-1,p[1]])
                            g.append([p[0]-1,p[1]])
                        if [p[0],p[1]+1] in wait:
                            wait.remove([p[0],p[1]+1])
                            g.append([p[0],p[1]+1])
                        if [p[0],p[1]-1] in wait:
                            wait.remove([p[0],p[1]-1])
                            g.append([p[0],p[1]-1])

            # print group,'g'
            for g in group:
                for p in g:
                    if adjent(p,pre):
                        for gi in g:
                            result.append(gi)
                        break
            pre=result[:]

            i+=1
            j+=1
        else:
            break
        for g in group:
            for p in g:
                if adjent(p,pre):
                    for gi in g:
                        result.append(gi)
                    break
        pre=[]
        for x in wait:
            if x in result:
                pre.append(x)

        i+=1
        j+=1
    # print result
    for i in xrange(n):
        for j in xrange(m):
            if [i,j] not in result and matrix[i][j]!='X':
                matrix[i][j]='X'
    print matrix

def circle(matrix,m,n,x,y):
    # global result
    wait=[]
    if x==m-x-1 and y==n-y-1:
        if matrix[y][x]=='o':
            wait.append([y,x])

    else:
        for i in xrange(x,m-x-1):
            if matrix[y][i]=='o':
                wait.append([y,i])
        for j in xrange(y,n-y-1):
            if matrix[j][m-x-1]=='o':
                wait.append([j,m-x-1])
        for i in xrange(m-x-1,x,-1):
            if matrix[n-y-1][i]=='o':
                wait.append([n-y-1,i])
        for j in xrange(n-y-1,y,-1):
            if matrix[j][x]=='o':
                wait.append([j,x])
    return wait

def adjent(p,list):
    for q in list:
        # print p,q
        if p[0]==q[0] and (p[1]==q[1]+1 or p[1]==q[1]-1):
            return True
        elif p[1]==q[1] and (p[0]==q[0]+1 or p[0]==q[0]-1):
            return True

    return False

# matrix=[[1,2,3,4],[8,9,4,3],[7,6,5,2]]
matrix=[['x','x','x','x','x'],['x','o','o','o','x'],['x','x','o','o','x'],['x','x','x','o','x'],['x','o','x','x','x']]
# matrix=["XXXXX","XOOOX","XXOOX","XXXOX","XOXXX"]
surround(matrix)