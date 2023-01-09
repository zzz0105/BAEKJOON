import sys
input = sys.stdin.readline

N = int(input())
price = [list(map(int,input().split())) for _ in range(N)]
answer = float('inf')

for i in range(3):
    dp = [[float('inf')]*3 for _ in range(N)]
    dp[0][i] = price[0][i]
    for j in range(N-1):
        dp[j+1][0] = price[j+1][0]+min(dp[j][1],dp[j][2])
        dp[j+1][1] = price[j+1][1]+min(dp[j][0],dp[j][2])
        dp[j+1][2] = price[j+1][2]+min(dp[j][0],dp[j][1])
    for j in range(3):
        if i!=j:
            answer = min(answer, dp[-1][j])
            
print(answer)