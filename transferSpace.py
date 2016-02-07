def transferSpace(s):
    s=list(s)
    count=0
    p=len(s)-1
    for x in s:
        if x==' ':
           s.append('')
           s.append('')
    x=len(s)-1
    while x>=0 and p>=0:
        # print s[x]
        if s[p]==' ':
            s[x]='0'
            x-=1
            s[x]='2'
            x-=1
            s[x]='%'
            x-=1
            p-=1
        else:
            s[x]=s[p]
            x-=1
            p-=1
    return ''.join(s)
print transferSpace("asd asd asd ")
