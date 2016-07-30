def isperfectSquare(n):
    if n<4:
        return False

    p=2.0
    while True:
        if n/p>p:
            p*=2
        elif n/p==p:
            # print n/p,p
            return True
        else:
            break
    q=p
    p=float(p//2)
    m=(p+q)//2
    # print n,p,q,m
    while p<=q:
         # print n,p,q,m
         if n/m>m:
             p=m+1
             m=(p+q)//2
         elif n/m<m:
             q=m-1
             m=(p+q)//2
         else:
             return True
    return False

print isperfectSquare(1000000000000000.0)

