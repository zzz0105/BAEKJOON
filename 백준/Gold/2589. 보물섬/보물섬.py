import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    dist = 0
    q = deque()
    q.append((i,j))
    visited = [[-1]*M for _ in range(N)]
    visited[i][j] = 0
    while q:
        i, j = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M and treasure_map[ni][nj]=='L' and visited[ni][nj]==-1:
                visited[ni][nj] = visited[i][j] + 1
                dist = max(dist, visited[ni][nj])
                q.append((ni,nj))
    return dist

N, M = map(int,input().split())
treasure_map = [list(input()) for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if treasure_map[i][j] == 'L':
            answer = max(answer, bfs(i,j))
print(answer)