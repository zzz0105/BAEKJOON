import heapq
import sys
heap = []
answer = []
n = int(input())
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    if x.isdecimal():
        x = int(x)
        if x > 0:
            heapq.heappush(heap, (-x, x))
        elif x == 0:
            answer.append(heapq.heappop(heap)[1] if heap else 0)
print(*answer, sep='\n')