numbers={
                '0':[' '],
                '1':['*'],
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
result=[]
def letterCombinations(digits,pre):
    if len(digits)==0:
        result.append(pre)
    else:
            poss=numbers[digits[0]]
            for j in poss:
                temp=pre
                temp+=j
                letterCombinations(digits[1:],temp)
digits='0123'

letterCombinations(digits,'')
print result