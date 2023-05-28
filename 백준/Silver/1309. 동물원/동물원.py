# 점화식: dp[i] = dp[i-2] + dp[i-1]*2

N = int(input())
dp = [[1]*3 for _ in range(N)]
# [i][0]:선택x [i][1]:왼쪽 선택 [i][2]: 오른쪽 선택
for i in range(1,N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[-1]) % 9901)