'''
PriorityQueue: 우선순위 큐
오름차순으로 정렬되는 특성을 가짐
lock을 제공하여 스레드로부터 안전. heap보다 속도가 느리다.
이 문제는 PriorityQueue로 풀면 시간 초과 발생...
'''
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    nums = map(int, sys.stdin.readline().rstrip().split())
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > n:
            heapq.heappop(heap)

print(heapq.heappop(heap))