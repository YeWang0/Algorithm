# [6,23][3,13][4,11]
total=17
values=[]
s={6:23,3:13,4:11}
def getmax(x):
    if s.get(x)!=None:
        return max(s.get(x),values[x])
    else:
        return values[x]
#
# value[1]=0
# value[2]=0
# value[3]=13
# value[4]=13
# value[5]=0
# value[6]=27
for i in xrange(total+1):
    values.append(0)
    for j in xrange((i+1)//2+1):

        r=getmax(j)+getmax(i-j)
        # print(i,j,i-j,'->',r)
        if r>values[i]:
            values[i]=r
    # print(values)
print(values)
