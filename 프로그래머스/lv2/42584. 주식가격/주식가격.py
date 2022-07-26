from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        p = prices.popleft()
        cnt = 0
        for price in prices:
            cnt += 1
            if p>price:
                break
        answer.append(cnt)
    return answer