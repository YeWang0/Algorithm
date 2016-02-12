def Say(n):
    def count(s):
        s+='.'
        t='.'
        c=0
        l=''
        for i in s:
            if t==i:
               c+=1
            else:
                if c!=0:
                    l+=str(c)
                    l+=t
                    c=1
                    t=i
                else:
                    c+=1
                    t=i
        return l
    s='1'
    for i in range(n-1):
        s=count(s)
        # print s
    return s

Say(5)
