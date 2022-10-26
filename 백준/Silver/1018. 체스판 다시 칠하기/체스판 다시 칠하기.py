import sys

def check(x,y):
    global board, ans
    tmp1 = 0
    tmp2 = 0
    for p in range(x,8+x):
        for q in range(y,8+y):
            if (p+q)%2:
                if board[p][q] != 'B':
                    tmp1 += 1
                else:
                    tmp2 += 1
            else:
                if board[p][q] != 'W':
                    tmp1 += 1
                else:
                    tmp2 += 1              
    ans = min(ans,tmp1,tmp2)

n, m = map(int,sys.stdin.readline().rstrip().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ans = 64
for i in range(n-8+1):
    for j in range(m-8+1):
        check(i, j)
print(ans)