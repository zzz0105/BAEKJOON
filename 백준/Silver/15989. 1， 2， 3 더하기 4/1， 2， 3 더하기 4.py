tc = int(input())
nums = [int(input()) for _ in range(tc)]
dp = [0]*(max(nums)+1)
for n in (3,2,1):
    dp[n] = 1
    for i in range(n,max(nums)+1):
        dp[i] += dp[i-n]
for num in nums:
    print(dp[num])