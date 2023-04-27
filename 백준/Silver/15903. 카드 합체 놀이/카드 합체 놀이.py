import heapq

n, m = map(int,input().split())
cards = list(map(int,input().split()))
heapq.heapify(cards)
for _ in range(m):
    plus = heapq.heappop(cards)+heapq.heappop(cards)
    for _ in range(2):
        heapq.heappush(cards, plus)
print(sum(cards))