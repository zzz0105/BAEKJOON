from collections import deque

n = int(input())
c = int(input())
connected = {}
visited = [0] * (n+1)
for _ in range(c):
    com1, com2 = map(int, input().split())
    connected[com1] = connected.get(com1, []) + [com2]
    connected[com2] = connected.get(com2, []) + [com1]

coms = deque()
coms.append(1)
while coms:
    com = coms.popleft()
    visited[com] = 1
    for co in connected[com]:
        if visited[co]==0:
            coms.append(co)

print(visited.count(1)-1)