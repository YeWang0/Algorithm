#
# def partition(s,n,x):
#     print s,n,x
#     if n<=1 and s[0]<=x:
#         return 1
#     if n<=1 and s[0]>x:
#         return 0
#     if n>1 and s[0]<=x:
#         return 1+partition(s[1:],n-1,x)
#     elif n>1 and s[n-1]>x:
#         return 1+partition(s[:len(s)-1],n-1,x)
#     else:
#         s[0],s[n-1]=s[n-1],s[0]
#         print s
#         return 1+partition(s[1:],n-2,x)
# s=[2,4,5,7,1,3,6]
# print partition(s,7,4)
# print s

def c(s):
    s[0],s[1]=s[1],s[0]
    if True:
        s=1
    else:
        s=2

s=[1,2,3]
c(s)
print s