from collections import deque
import sys
input = sys.stdin.readline

def bfs(b):
    q = deque([(b)])
    visited = [-1]*(N+1)
    visited[b] = 0
    while q:
        b = q. popleft()
        for nb in arr[b]:
            if visited[nb]==-1:
                q.append(nb)
                visited[nb] = visited[b]+1
    dist_dict = {}
    for b in range(1,N+1):
        dist_dict[visited[b]]=dist_dict.get(visited[b],[])+[b]
    max_dist = max(dist_dict)
    print(min(dist_dict[max_dist]),max_dist,len(dist_dict[max_dist]))

N, M = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
bfs(1)