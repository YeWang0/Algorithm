def maxSubArray(s):
    n=len(s)
    result=[0 for i in xrange(n)]
    max=0
    current=0
    for i in xrange(n):
        if current>=0:
            current+=s[i]
        else:
            current=s[i]
        if current>max:
            max=current

    return max

print maxSubArray([1,2,-1,4,-3,5,-2,7,-8])