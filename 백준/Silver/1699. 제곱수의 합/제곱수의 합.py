n = int(input())
dp = [100001]*(n+1)
dp[0] = 0
dp[1] = 1
for i in range(1,n+1):
    for j in range(1,int(i**(1/2)+1)):
        dp[i] = min(dp[i-j*j]+1,dp[i])
    dp[i] = min(dp[i-1]+1,dp[i])
print(dp[-1])