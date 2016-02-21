s='ABCDE'
result=[]
def Permutation(result,s,l,r):
    if l==r:
        # print s
        result.append(''.join(s))
    else:
        for i in range(l,r+1):
            s[i],s[l]=s[l],s[i]
            Permutation(result,s,l+1,r)
            s[i],s[l]=s[l],s[i]
Permutation(result,list(s),0,len(s)-1)
for i in result:
    print i
# result=set(result)
# r=[]
# for i in result:
#     r.append(''.join(i))
# print r
