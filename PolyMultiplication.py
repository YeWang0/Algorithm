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
a=[1,2,3,4]
b=[1,1,1,1]
polyMultiplication(a,b)