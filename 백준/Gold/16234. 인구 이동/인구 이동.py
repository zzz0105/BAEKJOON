from collections import deque
import sys
input = sys.stdin.readline

def union_check(i,j):
    global people, visited
    q = deque()
    q.append((i,j))
    union_country = set()
    union_country.add((i,j))
    union_people = people[i][j]
    while q:
        i, j = q.popleft()
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni, nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and (ni,nj) not in union_country:
                if L<=abs(people[i][j]-people[ni][nj])<=R:
                    q.append((ni,nj))
                    visited[ni][nj] = True
                    union_country.add((ni,nj))
                    union_people += people[ni][nj]
    union_country = tuple(union_country)
    avg_people = union_people // len(union_country)
    for x, y in union_country:
        people[x][y] = avg_people
    return True if len(union_country)>1 else False

N, L, R = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(N)]
day = 0

while True:
    changed = False
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                changed = union_check(i,j) or changed
    if not changed:
        break
    day += 1

print(day)