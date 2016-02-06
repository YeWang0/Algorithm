import re
def palidrome(s):
    m=re.findall(r'\w',s)
    return m==m[::-1]
print palidrome("as ,d, fgh jkl k,jh g,fd sa")