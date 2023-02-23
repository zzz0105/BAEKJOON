import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b, bridge, N):
  dq = deque([a])
  visited = [-1]*(N+1)
  visited[a] = 0
  while dq:
    now = dq.popleft()
    if now == b:
      break
    for i in range(now+bridge[now], N+1, bridge[now]):
      if visited[i] == -1:
        dq.append(i)
        visited[i] = visited[now]+1
    for i in range(now-bridge[now], 0, -bridge[now]):
      if visited[i] == -1:
        dq.append(i)
        visited[i] = visited[now]+1
  return visited[b] 

N = int(input())
bridge = [0] + list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, bridge, N))