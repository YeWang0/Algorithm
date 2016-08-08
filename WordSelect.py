def wordSelect(board,word):
    index=0
    for line in board:
        for i in line:
            if word[index]==i:
                print word[index],i
                index+=1
            if index>=len(word):
                print index,len(word)
                return True

    return False

board=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print  wordSelect(board,'ABCAC')
