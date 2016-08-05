def mySqrt(x):
    t=x//2
    while t>x//t:
        t=t//2
    p=t
    q=t*2
    m=(p+q)//2
    while p<=q:
        if m*m<x:
            p=m+1
        elif m*m>x:
            q=m-1
        else:
            return m
        m=(p+q)//2
    return m

print mySqrt()
