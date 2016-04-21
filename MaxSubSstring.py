def maxSubstring(a,b):
    try:
        if a[0]==b[0]:
            return 1+maxSubstring(a[1:],b[1:])
    except:
        return 0
    return max(maxSubstring(a,b[1:]),maxSubstring(a[1:],b))
a='aaabbbccc'
b='abcabcabc'

print maxSubstring(a,b)
