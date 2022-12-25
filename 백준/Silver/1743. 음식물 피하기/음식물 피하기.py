import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global passage, cnt
    cnt += 1
    passage[x][y] = False
    for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M:
            if passage[nx][ny] == True:
                dfs(nx,ny)

N, M, K = map(int,input().split())
passage = [[False]*M for _ in range(N)]
biggest = 0
for _ in range(K):
    r, c = map(int,input().split())
    passage[r-1][c-1] = True
for i in range(N):
    for j in range(M):
        if passage[i][j] == True:
            cnt = 0
            dfs(i, j)
            biggest = max(biggest, cnt)
print(biggest)