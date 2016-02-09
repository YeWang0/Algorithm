
def Max(s):
    if len(s)==1:
        return s[0]
    elif len(s)==2:
        return max(s[0],s[1])
    else:
        m=len(s)//2
        return max(Max(s[:m]),Max(s[m:]))

def compare(a,b):
    if a>b:
        return a,b
    else:
        return b,a

def MaxMin(s):
    print s
    if len(s)==2:
        return compare(s[0],s[1])
    elif len(s)==1:
        return s[0],s[0]
    else:
        mid=len(s)//2
        max1,min1=MaxMin(s[:mid])
        max2,min2=MaxMin(s[mid:])
        max,min=compare(max1,max2)[0],compare(min1,min2)[1]
        return max,min

s=[1,3,2,7,5,3,7,9,96,4,3,2,2,34,12]
# print Max(s)
print MaxMin(s)
