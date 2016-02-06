def rotate(string,offset):
    return string[len(string)-offset:]+string[:len(string)-offset]

s="abcdefg"
print rotate(s,1)