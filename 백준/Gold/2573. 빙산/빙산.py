from collections import deque
import sys
def bfs(x, y):
    global visited
    visited[x][y] = 1
    ice = deque()
    ice.append((x,y))
    while ice:
        x, y = ice.pop()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and iceberg[nx][ny] != 0:
                visited[nx][ny] = 1
                ice.append((nx,ny))

n, m = map(int, input().split())
iceberg = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
year = 0
while True:
    #몇 개의 덩어리로 나누어져있는지 확인
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    cnt0 = 0
    for x in range(n):
        cnt0 += iceberg[x].count(0)
        for y in range(m):
            if iceberg[x][y]!=0 and visited[x][y]==0:
                bfs(x,y)
                cnt += 1
            if cnt == 2:
                break
    if cnt == 2:
        break
    if cnt0 == n*m:
        year = 0
        break

    year += 1

    #주변 0의 개수 세기
    zero = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if iceberg[x][y] != 0:
                for dx, dy in move:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<n and 0<=ny<m and iceberg[nx][ny]==0:
                        zero[x][y] += 1
    for x in range(n):
        for y in range(m):
            iceberg[x][y] = max(iceberg[x][y]-zero[x][y],0)

print(year)