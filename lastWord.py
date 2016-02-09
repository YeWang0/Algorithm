# length of last word
def lastword(str):
    s=0
    count=0
    for x in str[::-1]:
        if x!=' ':
            s=1
        if s==1 and x!=' ':
            count+=1
        if s==1 and x==' ':
            return count
    return count
print(lastword("    "))