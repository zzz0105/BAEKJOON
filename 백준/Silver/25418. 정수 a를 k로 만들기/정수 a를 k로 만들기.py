from collections import deque

def make(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x==K:
            return(dp[K])
        for dx in (1, x):
            nx = x+dx
            if 0<=nx<1000001 and dp[nx]>dp[x]+1:
                dp[nx] = min(dp[nx],dp[x]+1)
                q.append(nx)

A, K = map(int,input().split())
dp = [float('inf')]*(1000001)
dp[A] = 0
print(make(A))