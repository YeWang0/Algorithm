def maxSubsequence(a,b,s):

    try:
        if a[0]==b[0]:
            return 1+maxSubsequence(a[1:],b[1:],s+a[0])
    except:
        return 0
    return max(maxSubsequence(a,b[1:],s),maxSubsequence(a[1:],b,s))
a='aaabbbccc'
b='abcabcabc'

print maxSubsequence(a,b,'')
