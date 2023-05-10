import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v, w):
    global distance
    for nv, nw in tree[v]:
        if distance[nv] == -1:
            distance[nv] = w+nw
            dfs(nv, w+nw)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

# 루트노드(1)에서 가장 먼 노드를 찾고, 그 노드 기준으로 가장 먼 노드를 찾는다
distance = [-1]*(n+1)
distance[1] = 0
dfs(1, 0)

idx = distance.index(max(distance))
distance = [-1]*(n+1)
distance[idx] = 0
dfs(idx, 0)

print(max(distance))