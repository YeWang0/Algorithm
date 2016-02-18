s=[[0,0,1,0],
   [1,1,1,0],
   [1,0,1,0],
   [0,1,1,0],
   [0,1,1,0]
   ]
bx=len(s)
by=len(s[0])

def look_around(s,x,y):

    if getpixol(s,x,y)<=0:
        return getpixol(s,x,y)
    else:
        r=0
        try:
            if getpixol(s,x+1,y)==1:r+=1
            if getpixol(s,x-1,y)==1:r+=2
            if getpixol(s,x,y+1)==1:r+=4
            if getpixol(s,x,y-1)==1:r+=8
        except:
            # print r
            return r
    return r

def getpixol(s,x,y):

    if x>=0 and x<bx and y>=0 and y<by:
        return s[x][y]
    else:
        return -1


def search(s,x,y):
    lx=x
    rx=x
    hy=y
    ly=y
    task=[[x,y]]
    finish=[]
    while task:
        t=task[0]
        # print t
        task=addtask(task,t[0],t[1],look_around(s,t[0],t[1]),finish)
        task.remove(t)
        finish.append(t)
    #
    # print finish
    findBoundary(finish,lx,rx,ly,hy)

def addtask(task,x,y,n,finish):
    # print x,y,n
    if n<1:
        return task
    else:
        for i in [1,-1]:
            t=n%2
            if t==1 and [x+i,y] not in finish and [x+i,y] not in task:
                task.append([x+i,y])

            n=n/2
        for i in [1,-1]:
            t=n%2
            if t==1 and [x,y+i] not in finish and [x,y+i] not in task:
                task.append([x,y+i])


            n=n/2
    # print task
    return task

def findBoundary(pixols,lx,rx,ly,hy):
    for i in pixols:
        if i[0]<lx:
            lx=i[0]
        elif i[0]>rx:
            rx=i[0]
        if i[1]>hy:
            hy=i[1]
        elif i[1]<ly:
            ly=i[1]
    print 'Min Boundary:\n\tX:{0},Y:{1}'.format([lx,rx],[ly,hy])



search(s,2,2)