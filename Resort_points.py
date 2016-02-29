
def resort(s,n):
    l=[[]for i in xrange(n)]
    r=[]
    # print len(l)
    for i in s:
        l[i[1]].append(i)
    # print l
    for i in l:
        for j in i:
            r.append(j)
    print r

resort([[1,2],[1,3],[3,4],[5,2]],6)
