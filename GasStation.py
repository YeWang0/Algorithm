def canCircuit(gas,cost):
    poss=[0 for i  in len(gas)]
    for i in len(gas):
        if gas[i]>=cost[i]:
            poss[i]=1
            