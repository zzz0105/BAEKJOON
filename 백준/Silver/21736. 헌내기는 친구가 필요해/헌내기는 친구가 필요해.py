import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c):
    global visited, meet
    for nr, nc in ((r+1,c),(r,c+1),(r-1,c),(r,c-1)):
        if 0<=nr<N and 0<=nc<M and campus[nr][nc]!='X' and not visited[nr][nc]:
            visited[nr][nc] = True
            if campus[nr][nc] == 'P':
                meet += 1
            dfs(nr, nc)

N, M = map(int, input().split())
campus = []
dy = (-1,-1)
visited = [[False]*M for _ in range(N)]
meet = 0
for i in range(N):
    campus.append(tuple(input()))
    for j in range(M):
        if campus[-1][j]=='I':
            dy = (i, j)
            visited[i][j] = True
            break
dfs(*dy)
print(meet if meet else 'TT')