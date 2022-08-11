import heapq
import sys
heap = []
answer = []
n = int(input())
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        answer.append(heapq.heappop(heap)[1] if heap else 0)
print(*answer, sep='\n')