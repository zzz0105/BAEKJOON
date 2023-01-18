from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q = deque([x])
    parent=[0]*(N+1)
    parent[1]= 1
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if parent[nx] == 0:
                parent[nx] = x
                q.append(nx)
    return parent[2:]

N = int(input())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
print(*bfs(1), sep='\n')