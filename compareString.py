def anagrams(s1,s2):
    d1=dict()
    for x in s1:
        if d1.get(x)==None:
            d1[x]=1
        else:
            d1[x]+=1
    for x in s2:
        if d1.get(x)==None:
            return False
        else:
            d1[x]-=1
            if d1[x]<0:
                return False
    return True


print anagrams("hwheq","hwe")
# print(sorted("asasfas"))