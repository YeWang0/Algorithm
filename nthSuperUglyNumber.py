def nthSuperUglyNumber(n,primes):
    result=[float('inf') for i in xrange(n)]
    result[0]=1
    index=[0 for i in xrange(len(primes))]
    for i in xrange(1,n):
        for j in xrange(len(primes)):
            result[i]=min(result[i],result[index[j]]*primes[j])
        print result
        for j in xrange(len(primes)):
            if result[i]==result[index[j]]*primes[j]:
                index[j]+=1
    return result[-1]
print nthSuperUglyNumber(10,[2,3,11])