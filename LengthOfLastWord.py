def lastword(s):
    l=s.split(' ')
    for i in l[::-1]:
        if len(i)!=0:
            return len(i)
    return 0

s='hello world    '

lastword('')