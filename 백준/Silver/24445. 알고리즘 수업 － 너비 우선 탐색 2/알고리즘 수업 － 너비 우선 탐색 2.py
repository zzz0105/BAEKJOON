import sys
input = sys.stdin.readline
from collections import deque

def bfs(R):
  q = deque([R])
  cnt = 1
  visited = [0]*(N+1)
  visited[R] = cnt
  while q:
    now = q. popleft()
    for i in graph[now]:
      if not visited[i]:
        q.append(i)
        cnt += 1
        visited[i] = cnt
  return visited[1:]

N, M, R = map(int,input().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
  u, v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
for i in range(1, N+1):
  graph[i].sort(reverse=True)
print(*bfs(R), sep='\n')