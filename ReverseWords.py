import re
def reverseWords(s):
    s=s.split(' ')
    try:
        while 1:
            s.remove('')
    except:
        print(s)
def getwords(s):
     m=re.findall(r'[\w]+',s)
     return m
