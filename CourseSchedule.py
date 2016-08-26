def courseSchedule(numCourses, prerequisites):
    # kahn's algorithm
    start=dict()
    end=dict()
    for p in prerequisites:
        if p[0] not in start.keys():
            start[p[0]]=1
        else:
            start[p[0]]+=1
        if p[1] not in end.keys():
            end[p[1]]=1
        else:
            end[p[1]]+=1

    s=[]
    l=[]
    for st in start.keys():
        if st not in end.keys():
            s.append(st)

    while s:
        print s,'s'
        temp=s.pop(0)
        l.append(temp)
        remove=[]
        for p in prerequisites:
            print p
            if p[0]==temp:
                if end[p[1]]==1:
                    s.append(p[1])
                end[p[1]]-=1
                remove.append(p)
        for i in remove:
            prerequisites.remove(i)
    print l

prerequisites=[
    [8,9],
    [1,4],
    [1,2],
    [4,2],
    [4,3],
    [3,2],
    [5,2],
    [3,5],
    [8,2],
    [8,6]
]

courseSchedule(1,prerequisites)


