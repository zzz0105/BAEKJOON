import heapq

a, b = map(int, input().split())
heap = []
heapq.heappush(heap,a)
nums = {a: 1}

while True:
    n = heapq.heappop(heap)
    if n*2 <= b:
        nums[n*2] = nums[n] + 1
        heapq.heappush(heap, n*2)
    if n * 10 + 1 <= b:
        nums[n * 10 + 1] = nums[n] + 1
        heapq.heappush(heap, n * 10 + 1)
    if n*2 > b and n * 10 + 1 > b:
        break

try:
    print(nums[b])
except:
    print(-1)