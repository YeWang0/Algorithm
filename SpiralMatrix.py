# set n
n=10

m=[[]for i in xrange(0,n)]
for i in xrange(n):
    for j in xrange(n):
        m[i].append(0)
for i in m:
    print i
x=0
y=0
t=n
c=1
def spiral():
    global x,y,t,c,m
    for i in xrange(0,t):
        m[x][y+i]=c
        c+=1
    t-=1
    for i in xrange(0,t):
        m[x+1+i][y+t]=c
        c+=1
    for i in xrange(t-1,-1,-1):
        m[x+t][y+i]=c
        c+=1

    for i in xrange(t-1,0,-1):
        m[x+i][y]=c
        c+=1
while t>=1:
    spiral()
    x+=1
    y+=1
    t-=1

for i in m:
    print i


