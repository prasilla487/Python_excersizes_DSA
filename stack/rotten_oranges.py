#caluculate minimum time rot all oranges
# the matric c*r 0: empty cell 1: fresh orange 2: rotten orange
r=3
c=5

def isSafe(i,j):
    if (i>=0 and i < r and j >=0 and j <c):
        return True
    return False

def minTime(matrix, r, c):
    changed = False
    num = 2
    while True:
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 2:
                    if isSafe(i-1, j) and matrix[i-1][j] == 1:
                        matrix[i-1][j] +=1
                        changed = True
                    if isSafe(i, j-1) and matrix[i][j-1] == 1:
                        matrix[i][j-1] +=1
                        changed = True

                    if isSafe(i+1, j) and matrix[i+1][j] == 1:
                        matrix[i+1][j] +=1
                        changed = True

                    if isSafe(i, j+1) and matrix[i][j+1] == 1:
                        matrix[i][j+1] +=1
                        changed = True
                        
        
            if changed:
                changed = False
                num +=1

        if not changed:
                break
        

    for row in range(r):
        for column in range(c):
            if matrix[row][column] == 1:
                return -1

        
    return num-2


if __name__ == "__main__":
   # matrix = [[2,1,0,2,1],[1,0,1,2,1],[1,0,0,2,1]]
    matrix = [[1,2,1,0,1],[0,2,0,1,2],[1,1,0,1,2]]
    time = minTime(matrix, 3,5)
    print('time required is {}'.format(time))


