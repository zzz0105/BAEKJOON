from collections import deque
import sys

def get_dist(fp,fq):
    global move, n, m, arr
    pos = deque()
    pos.append((fp,fq))
    visited = [[0]*m for _ in range(n)]
    visited[fp][fq] = 1
    while pos:
        p, q = pos.popleft()
        for dp, dq in move:
            np = p + dp
            nq = q + dq
            if 0<=np<n and 0<=nq<m and not visited[np][nq]:
                if arr[np][nq]==0:
                    pos.append((np,nq))
                    visited[np][nq] = visited[p][q] + 1
                else:
                    return visited[p][q]

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
move = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            answer = max(get_dist(i,j), answer)
print(answer)