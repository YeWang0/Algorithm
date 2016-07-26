def getsum(a,b):
    print a^b,a&b
    x=4
    while x:
        if a&b==0:
            return a^b
        else:
            a,b=a^b,(a&b)<<1
            print a,b
            print bin(a),bin(b)
            x-=1


