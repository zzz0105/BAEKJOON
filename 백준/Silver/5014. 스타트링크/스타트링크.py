from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q = deque([x])
    visited = [-1]*(F+1)
    visited[x] = 0
    while q:
        x = q.popleft()
        if x == G:
            return visited[x]
        for nx in (x+U, x-D):
            if 0<nx<=F and visited[nx]==-1:
                visited[nx] = visited[x]+1
                q.append(nx)
    return "use the stairs"

F, S, G, U, D = map(int,input().split())
print(bfs(S))