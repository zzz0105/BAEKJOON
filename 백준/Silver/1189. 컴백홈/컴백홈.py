import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c):
    global visited, cnt
    if r==house[0] and c==house[1] and visited[r][c]==K:
        cnt += 1
        return
    for nr, nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
        if 0<=nr<R and 0<=nc<C and graph[nr][nc]!='T' and not visited[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc)
            visited[nr][nc] = 0

R, C, K = map(int,input().split())
graph = tuple(tuple(input()) for _ in range(R))
visited = [[0]*C for _ in range(R)]
hansu = (R-1, 0)
house = (0, C-1)
visited[hansu[0]][hansu[1]] = 1
cnt = 0
dfs(*hansu)
print(cnt)