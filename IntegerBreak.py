s=[0,1,2,3,4]

def integerBreak(n):
    for i in xrange(n+1):
        if i >=len(s):
            max=i
            for x in xrange(2,i//2+1):
                if s[x]*s[i-x]>max:
                    max=s[x]*s[i-x]
            s.append(max)

integerBreak(100)
print s
