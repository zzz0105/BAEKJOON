import sys
input = sys.stdin.readline

def guess(n):
    if len(zeros) == n:
        for i in range(9):
            print(*sudoku[i],sep='')
        exit()
    i, j = zeros[n]
    for num in range(1,10):
        if check(i, j, num):
            sudoku[i][j] = num
            guess(n+1)
            sudoku[i][j] = 0

def check(x, y, num):
    for ny in range(9):
        if sudoku[x][ny]==num:
            return False
    for nx in range(9):
        if sudoku[nx][y]==num:
            return False
    nx = (x//3)*3
    ny = (y//3)*3
    for dx in range(3):
        for dy in range(3):
            if sudoku[nx+dx][ny+dy] == num:
                return False
    return True

sudoku = [list(map(int,list(input().rstrip()))) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            zeros.append((i,j))
guess(0)