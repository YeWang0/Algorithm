def restoreIP(s):
    result=[]
    def restore(i,j,k):
        if (s[0]=='0' and i>1) or (s[i]=='0' and j-i>1) or (s[j]=='0' and k-j>1) or (s[k]=='0' and n-k>1):
                return

        if int(s[:i])<256 and int(s[i:j])<256 and int(s[j:k])<256 and int(s[k:])<256:
            result.append((s[:i])+'.'+(s[i:j])+'.'+(s[j:k])+'.'+(s[k:]))
    n=len(s)
    for i in xrange(1,4):
        for j in xrange(i+1,min(n,i+4)):
            for k in xrange(j+1,min(n,j+4)):
                # print i,j,k
                if k>n-4:
                    restore(i,j,k)
    print result

s="010010"
restoreIP(s)