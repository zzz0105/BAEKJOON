import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v,w):
    global distance
    for nv,nw in graph[v]:
        if distance[nv] == -1:
            distance[nv] = w+nw
            dfs(nv,w+nw)

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    v, *info = map(int, input().split())
    for i in range(len(info)//2):
        nv, dist = info[i*2], info[i*2+1]
        graph[v].append((nv, dist))

# 아무 구슬(1)을 기준으로 가장 거리가 먼 구슬을 구한다
# 그 구슬을 기준으로 가장 거리가 먼 구슬까지가 그 트리의 지름이다
distance = [-1]*(V+1)
distance[1] = 0
dfs(1, 0)
idx = distance.index(max(distance))
distance = [-1]*(V+1)
distance[idx] = 0
dfs(idx, 0)
print(max(distance))