def canCircuit(gas,cost):
    poss=[0 for i  in len(gas)]
    result=[]
    for i in len(gas):
        if gas[i]>=cost[i]:
            poss[i]=1
    def check(index):
        left=0
        for i in xrange(index,len(gas)):
            temp=gas[i]-cost[i]
            if temp+left>0:
                left=temp+left
            else:
                return False
        for i in xrange(0,index):
            temp=gas[i]-cost[i]
            if temp+left>0:
                left=temp+left
            else:
                return False
        return True
    for i in len(gas):
        if i==1:
            if check(i):
                result.append(i)
    return result
