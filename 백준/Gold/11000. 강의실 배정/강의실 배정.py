import heapq, sys
input = sys.stdin.readline

N = int(input())
hq = []
heapq.heappush(hq, 0)

classroom = sorted([tuple(map(int, input().split())) for _ in range(N)])
for s, t in classroom:
    ct = heapq.heappop(hq)
    if ct > s:
        heapq.heappush(hq, ct)
    heapq.heappush(hq, t)

print(len(hq))
