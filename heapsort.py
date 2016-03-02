import random
def heapbuilder(s):
    for x in xrange(len(s)):
        i=x+1
        while i//2>0 and s[i-1]>s[i//2-1]:
            s[i-1],s[i//2-1]=s[i//2-1],s[i-1]
            i=i//2
    return s
def sort(s):
    for x in xrange(len(s),1,-1):
        s=heapbuilder(s[:x])+s[x:]
        s[0],s[x-1]=s[x-1],s[0]
    return s

s=[]
for i in xrange(1000):
    s.append(random.randint(1, 1000))
# print heapbuilder(s)
print sort(s)