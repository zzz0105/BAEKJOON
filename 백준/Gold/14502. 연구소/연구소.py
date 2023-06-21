from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

def bfs():
    safe = 0
    dq = deque()
    visited = [[False]*M for _ in range(N)]
    for i, j in virus:
        dq.append((i,j))
        visited[i][j] = 0
    while dq:
        i, j = dq.popleft()
        for ni, nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and lab[ni][nj]==0:
            # 아직 퍼지지 않았고 빈 칸이라면
                visited[ni][nj] = True
                dq.append((ni,nj))
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and lab[i][j]==0:
                safe += 1
    return safe

N, M = map(int,input().split())
lab = []
virus = []  # 바이러스 위치
empty = []  # 벽을 세울 수 있는 빈 칸 위치
for i in range(N):
    lab.append(list(map(int,input().split())))
    for j in range(M):
        if lab[-1][j] == 2:
            virus.append((i,j))
        elif lab[-1][j] == 0:
            empty.append((i,j))

max_safe = -1
for cb in combinations(empty,3):
    for i, j in cb:     # 벽 세운다
        lab[i][j] = 1
    max_safe = max(max_safe, bfs())
    for i, j in cb:     # 벽 없앤다
        lab[i][j] = 0
print(max_safe)