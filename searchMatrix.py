def searchMatrix(matrix,target):
    n=len(matrix)
    for i in xrange(n):
        if target == matrix[i][0]:
            return True
        if target < matrix[i][0]:
            i-=1
            break
    # print i
    if i==-1:
        return False

    if matrix[i][-1]==target:
        return True
    if target<matrix[i][-1]:
        # binary search
        x=0
        y=len(matrix[i])-1
        mid=(x+y)//2
        # print x,y,mid
        while x<=y:
            if matrix[i][mid]==target:
                return True
            elif matrix[i][mid]>target:
                y=mid-1
            else:
                x=mid+1
            mid=(x+y)//2
    return False

matrix=[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
for i in matrix:
    for j in i:
        print searchMatrix(matrix,j)
