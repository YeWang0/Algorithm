def  Insert_sort(s,n):

    if n>1:
        Insert_sort(s,n-1)
        insert(s,n-1)

def insert(s,i):
    if i>0 and s[i]<s[i-1]:
        s[i],s[i-1]=s[i-1],s[i]
        insert(s,i-1)

s=[10,3,22,7,5,3,7,9,96,4,3,2,2,34,12,1]

Insert_sort(s,len(s))
print  s