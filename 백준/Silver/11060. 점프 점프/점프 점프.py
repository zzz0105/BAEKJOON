n = int(input())
a = tuple(map(int,input().split()))
dp = [float('inf')] * n
dp[0] = 0
for i in range(n):
  for j in range(1,a[i]+1):
    if 0<=i+j<n:
      dp[i+j] = min(dp[i]+1, dp[i+j])
print(dp[-1] if dp[-1]!=float('inf') else -1)