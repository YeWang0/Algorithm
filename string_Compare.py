def compareString(s1,s2):
    for i in xrange(len(s1)-len(s2)+1):
        for j in xrange(len(s2)):
            if s1[i+j]!=s2[j]:
                break
            if j==len(s2)-1:
                return i
    return -1

s1=""
s2=""
print(compareString(s1,s2))