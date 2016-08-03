def compareStr(a,b):
    x=list(b)
    print x,
    if a==b:
        return True

print compareStr('abc','cba')

def groupAnagrams(strs):
    dict={}
    for i in strs:
        temp=''.join(sorted(i))

        if temp not in dict:
            dict[temp]=[i]
        else:
            dict[temp].append(i)
    result=[]
    for i in dict.keys():
        result.append(dict[i])
    return result
groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])