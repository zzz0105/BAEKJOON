import heapq, sys

def dijkstra(start, end):
    costs = [float('inf')]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    costs[start] = 0
    while q:
        cost, v = heapq.heappop(q)
        if costs[v] < cost :
            continue
        for connected in bus_info[v]:
            new_cost = cost + connected[1]
            if new_cost < costs[connected[0]]:
                costs[connected[0]] = new_cost
                heapq.heappush(q,(new_cost,connected[0]))
    return costs[end]

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
bus_info = [[] for _ in range(n+1)]

for _ in range(m):
    start,end,cost = map(int,sys.stdin.readline().rstrip().split())
    bus_info[start].append((end,cost))
start, end = map(int,sys.stdin.readline().rstrip().split())

print(dijkstra(start, end))