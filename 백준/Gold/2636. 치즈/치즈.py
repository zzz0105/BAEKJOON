import sys
from collections import deque
input = sys.stdin.readline

def melt(i, j):
    global cheese
    q = deque([(i,j)])
    visited = [[0]*C for _ in range(R)]
    melt = set()
    while q:
        r, c = q.popleft()
        for nr, nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
                if cheese[r][c]==0:
                    q.append((nr,nc))
                    visited[nr][nc] = True
                    if cheese[nr][nc]==1:   # 공기 중에 노출된 치즈
                        melt.add((nr,nc))   
    for mr, mc in melt:
        cheese[mr][mc] = 0
    return len(melt)

R, C = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(R)]
melted = [1]    # while문 조건때문에 임의로 1을 넣어줌
while melted[-1]!=0:
    melted.append(melt(0,0))
print(len(melted)-2, melted[-2], sep='\n')