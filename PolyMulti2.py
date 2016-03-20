# karatsuba

def add(a,b,n):
    c=[]

    for i in xrange(n):
        c.insert(0,0)
    for i in b:
        c.append(i)
    if len(a)>len(c):
        a,c=c,a
    for i in xrange(len(a)):
        c[i]+=a[i]
    return c
def negative(x):
    y=[]
    for i in xrange(len(x)):
        y.append((-x[i]))
    return y

def PolyMulti2(a,b):
    x=len(a)
    y=len(b)
    if x>y:
        a,b=b,a
        x=len(a)
        y=len(b)
    if len(a)==1:
        print a,b,x,y
        c=[]
        for i in xrange(y):
            c.append(a[0]*b[i])
        return c
    a0=a[:x//2]
    a1=a[x//2:]
    b0=b[:y//2]
    b1=b[y//2:]
    Y=PolyMulti2(add(a0,a1,0),add(b0,b1,0))
    U=PolyMulti2(a0,b0)
    Z=PolyMulti2(a1,b1)
    Un=negative(U)
    Zn=negative(Z)
    z=x//2+y//2
    u=z//2
    return add(U,add(add(Y,add(Un,Zn,0),0),Z,u),z-u)


def polyMultiplication(a,b):
    x=len(a)
    y=len(b)
    l=[]
    for i in xrange(x+y-1):
        l.append(0)
    for i in xrange(x):
        for j in xrange(y):
            l[i+j]+=a[i]*b[j]
    print l

a=[2,2,2,0,2]
b=[0,1,1,1,1]
print PolyMulti2(a,b)

polyMultiplication(a,b)



