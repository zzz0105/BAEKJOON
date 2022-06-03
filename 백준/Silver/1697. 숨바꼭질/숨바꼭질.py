def seek():
    n_p = deque()   #수빈이 위치
    n_p.append(n)
    while n_p:
        x = n_p.popleft()   #현재 수빈이 위치
        if x==k:
            break
        for dx in [-1, 1, x]:
            nx = x+dx
            if nx in range(d+1) and arr[nx]==-1:
                arr[nx] = arr[x] + 1
                n_p.append(nx)

from collections import deque
n, k = map(int, input().split())    #수빈, 동생
d = 100000    #위치의 최대값
arr = [-1]*(d+1)    #0이상 100000이하
arr[n] = 0
seek()
print(arr[k])