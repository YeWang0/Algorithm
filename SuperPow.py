def superpow(a,b):
    #     b is []
    modulus=1337
    base=a
    result=1
    for i in b[::-1]:
        if i!=0:
            result=(result*pow(base,i))%modulus
        base=pow(base,10)%modulus
    print result


superpow(2,[1,0,0])
