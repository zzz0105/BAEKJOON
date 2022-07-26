from collections import deque
def solution(priorities, location):
    d_priorities = deque(list(enumerate(priorities)))
    cnt = 0
    while d_priorities:
        i, j = d_priorities.popleft()
        if j==max(priorities):
            cnt += 1
            priorities.remove(j)
            if i==location:
                return cnt
        else:
            d_priorities.append((i, j))