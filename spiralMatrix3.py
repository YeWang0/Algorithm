def generateMatrix(n):
    A = [[n*n]]
    while A[0][0] > 1:
        A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
    return A * (n>0)

print generateMatrix(10)

# A=[[4,5],[9,6],[8,7]]
# print A[::-1]
# print zip(*A[::-1])
# print zip(*A)