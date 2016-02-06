def anagrams(s1,s2):
    d1=dict()
    d2=dict()
    for x in s1:
        if d1.get(x)==None:
            d1[x]=1
        else:
            d1[x]+=1
    for x in s2:
        if d1.get(x)==None:
            d2[x]=1
        else:
            d2[x]+=1
    # print d1,d2
    if d1==d2:
        return True
    else:
        return False

print anagrams("hwheq","hweqh")
# print(sorted("asasfas"))