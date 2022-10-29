import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
dp = [0]*(k+1)
for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    if w > k:
        continue
    for i in range(k,0,-1):
        if i+w <= k and dp[i] != 0:
            dp[i+w] = max(dp[i]+v, dp[i+w])
    dp[w] = max(dp[w],v)
    
print(max(dp))