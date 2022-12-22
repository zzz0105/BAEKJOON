from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, start):
    q = deque()
    q.append(start)
    order = 1
    visited = [0]*(N+1)
    visited[start] = order
    while q:
        v = q.popleft()
        graph[v].sort()
        for con in graph[v]:
            if visited[con]==0:
                order += 1
                visited[con]=order
                q.append(con)
    return visited

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
print(*dfs(graph, R)[1:], sep='\n')