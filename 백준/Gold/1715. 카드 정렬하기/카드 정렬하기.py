import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

answer = 0
while len(cards) > 1:
    cc = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, cc)
    answer += cc
    
print(answer)