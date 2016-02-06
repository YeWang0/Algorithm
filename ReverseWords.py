import re
def reverseWords(s):
    s=s.split(' ')
    try:
        while 1:
            s.remove('')
    except:
        return s[::-1]
def getwords(s):
     m=re.findall(r'[\w]+',s)
     return m[::-1]

print(getwords("a b c d e f"))
