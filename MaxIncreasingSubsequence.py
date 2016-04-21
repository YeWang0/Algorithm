result=set()
def MaxIncreasingSubsequence(s,n,str):
    try:
        if s[0]>n:
            x=str[:]
            str.append(s[0])
            return max(1+MaxIncreasingSubsequence(s[1:],s[0],str),MaxIncreasingSubsequence(s[1:],n,x))
    except:
        if tuple(str) not in result:
            result.add(tuple(str))
        return 0

    return MaxIncreasingSubsequence(s[1:],n,str)

s=[1,2,3,5,2,1,4,2,23,12,2,3,1,2,3,5,123,1,123,11,222]

l=MaxIncreasingSubsequence(s,s[0]-1,[])
for i in result:
    if len(i)==l:
        print i
